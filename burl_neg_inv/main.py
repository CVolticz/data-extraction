from pathlib import Path
import pandas as pd
import numpy as np

import uuid
from burl_database.lib.SQLServerDatabaseConnector import SQLServerDatabaseConnector
from joblib import Parallel, delayed


def process(chunk, path):
    """
        Function for Parallel Processing
    """
    unique = uuid.uuid4()
    print(f"Processing File: {unique}")
    chunk.to_csv(f"{path}/file_{unique}.csv")
    return


def fetch_data_sls(start_date, end_date):


    query_stmt = f"""SELECT *,
                        str.STORE_SRCNUM AS STORE,
                        cls.CLASS
                    FROM F_SLS_SKU_STR_D s
                    INNER JOIN (
                        SELECT DISTINCT cl.DB_DIV_NO || lpad(class_displaynum, 3, 0) AS CLASS, 
                            cl.SKU_ID, cl.CLASS_DISPLAYNUM, cl.CLASS_DESC
                        FROM L_SKU cl 
                        WHERE (cl.CLASS_DISPLAYNUM <> '889'
                                AND cl.CLASS_ID not in (4000039, 4000048, 2300024, 2800014, 1200060, 4000044, 4000067, 4000011, 4000028, 4000043, 4000008, 4000031, 4000020, 4000017, 4000019, 4000066, 6300024)
                                AND cl.CLASS_ID not in (4000009, 4000076, 4400010, 4000047, 4000003, 4000006, 2900023, 5800001, 1800029, 4200053)
                                AND cl.CLASS_ID not in (4000051, 4000042, 5700003)
                                AND cl.SUBCATEGORY_ID <> 0
                                AND cl.SUBCATEGORY_ID IS NOT null)
                    ) cls ON cls.SKU_ID = s.SKU_ID
                    INNER JOIN ( SELECT st.STORE_ID, st.STORE_SRCNUM, st.STORE_DESC FROM L_STORE st ) str
                    ON s.STORE_ID=str.STORE_ID
                    WHERE s.DATE_ID >= '{start_date}' AND s.DATE_ID <= '{end_date}'
                    ORDER BY s.DATE_ID, str.STORE_SRCNUM, s.SKU_ID;            
                """
    
    # query_stmt = f"""SELECT EXTRACT( MONTH FROM s.DATE_ID ) AS MONTH, 
    #                     str.STORE_SRCNUM AS STORE,
    #                     MAX(str.REGION_DESC) AS TERRITORY,
    #                     cls.CLASS as CLASS,
    #                     MAX(cls.CL_DIVISION) AS DIVISION,
    #                     SUM(s.SLS_UNTS) AS NUM_UNTS_SLS,
    #                     SUM(CASE WHEN s.MD_TYPE=3 THEN 1 ELSE 0 END) AS NUM_MKD,
    #                     SUM(CASE WHEN s.RETRN_FLG=1 THEN 1 ELSE 0 END) AS NUM_RETRN
    #                 FROM F_SLS_SKU_STR_D s
    #                 INNER JOIN (
    #                     SELECT DISTINCT cl.DB_DIV_NO || lpad(class_displaynum, 3, 0) AS CLASS, 
    #                         cl.SKU_ID, cl.CLASS_DISPLAYNUM, cl.CLASS_DESC,
    #                         cl.MERCH_DIV_FLR_SEC_DESC AS CL_DIVISION
    #                     FROM L_SKU cl 
    #                     WHERE (cl.CLASS_DISPLAYNUM <> '889'
    #                             AND cl.CLASS_ID not in (4000039, 4000048, 2300024, 2800014, 1200060, 4000044, 4000067, 4000011, 4000028, 4000043, 4000008, 4000031, 4000020, 4000017, 4000019, 4000066, 6300024)
    #                             AND cl.CLASS_ID not in (4000009, 4000076, 4400010, 4000047, 4000003, 4000006, 2900023, 5800001, 1800029, 4200053)
    #                             AND cl.CLASS_ID not in (4000051, 4000042, 5700003)
    #                             AND cl.SUBCATEGORY_ID <> 0
    #                             AND cl.SUBCATEGORY_ID IS NOT null)
    #                 ) cls ON cls.SKU_ID = s.SKU_ID
    #                 INNER JOIN ( SELECT st.STORE_ID, st.STORE_SRCNUM, st.STORE_DESC, st.REGION_DESC FROM L_STORE st ) str
    #                 ON s.STORE_ID=str.STORE_ID
    #                 WHERE s.DATE_ID >= '{start_date}' AND s.DATE_ID <= '{end_date}'
    #                 GROUP BY str.STORE_SRCNUM, cls.CLASS, MONTH;            
    #             """


    print("Running Sales Query----")
    ssd = start_date.replace("-", "")
    eed = end_date.replace("-", "")

    path = f"./data/01_raw/sls_ts_data_{ssd}-{eed}"
    with sqldb as db:
        chunks = pd.read_sql_query(query_stmt, db, chunksize=2000000)
        Parallel(n_jobs=4, timeout=99999)(delayed(process)(chunk, path) for chunk in chunks)



if __name__ == "__main__":
    start_date="2021-08-01"
    end_date="2021-08-31"
    # month = "03-2022"

    result = fetch_data_sls(start_date, end_date) 