import requests
import csv
import json


def saveContentToCsv(fileName: str, data: list):
    """Save a query result as local csv file.

    Args:
        fileName (str): the name for the csv file.
        data (list): the query results.
        docPath (str, optional): folder path. Defaults to ''.
    """

    print(f"Saving data for {fileName}...\n")
    with open(fileName, "w", newline="") as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
        writer.writerows(data)


if __name__ == "__main__":
    files = [
        {
            "name": "qr_code.csv",
            "query": """SELECT p.reference as "SKU","" as "FAMILY", CONCAT("italiangres.com/",p.id_product,"-.html?utm_source=qr") as URL
            FROM ps_product AS p
            ORDER BY p.reference;""",
        },
        {
            "name": "etichette.csv",
            "query": """SELECT tmp.id, tmp.Reference, tmp.Manufacturer, tmp.Model, tmp.Color, ps_product.active as "Active", tmp.Spessore, tmp.Superficie
                FROM (
                    SELECT p.id_product AS "id", p.reference AS "Reference", m.name AS "Manufacturer", fvl.value AS "Model", fvl2.value AS "Color", 1 AS "Active", COALESCE(fvl3.value, '') AS "Spessore", COALESCE(flv5.Superficie, '') AS "Superficie"
                    FROM ps_product AS p
                    LEFT JOIN ps_product_lang AS pl ON p.id_product = pl.id_product
                    LEFT JOIN ps_manufacturer AS m ON p.id_manufacturer = m.id_manufacturer
                    LEFT JOIN ps_feature_product AS fp ON p.id_product = fp.id_product
                    LEFT JOIN ps_feature_value_lang AS fvl ON fp.id_feature_value = fvl.id_feature_value AND fvl.id_lang = 4
                    LEFT JOIN ps_feature_product AS fp2 ON p.id_product = fp2.id_product
                    LEFT JOIN ps_feature_value_lang AS fvl2 ON fp2.id_feature_value = fvl2.id_feature_value AND fvl2.id_lang = 4
                    LEFT JOIN ps_feature_product AS fp3 ON p.id_product = fp3.id_product
                    LEFT JOIN ps_feature_value_lang AS fvl3 ON fp3.id_feature_value = fvl3.id_feature_value AND fvl3.id_lang = 4
                    LEFT JOIN (SELECT p.id_product as "id", fvl.value as "Superficie" 
                        FROM ps_product AS p 
                        LEFT JOIN ps_feature_product AS fp ON p.id_product = fp.id_product 
                        LEFT JOIN ps_feature_value_lang AS fvl ON fp.id_feature_value = fvl.id_feature_value 
                        WHERE fvl.id_lang = 4 
                        AND fp.id_feature = 15
                        ORDER BY p.reference) AS flv5 ON p.id_product = flv5.id
                    WHERE fp.id_feature = 56 AND fp2.id_feature = 57 AND pl.id_lang = 4
                    GROUP BY p.id_product
                    ORDER BY p.id_product) AS tmp
                JOIN ps_product ON tmp.id = ps_product.id_product
                WHERE ps_product.active = 1;""",
            "dataFunction": lambda row: list(row[:7]) + [row[7].split(" ")[0] if row[7] else ""]
        },
    ]
    apiKey = ''

    for file in files:
        print(f"Calling the API for {file["name"]}")
        response = requests.post(
            "https://11getnrgna.execute-api.eu-central-1.amazonaws.com/default/AggiornamentoCsvSpedizioni",
            headers={
                "x-api-key": apiKey,
                "Accept": "application/json",
            },
            data=json.dumps(file["query"])
        )
        
        if 200 <= response.status_code <= 300:
            data = json.loads(response.content)

            try:
                data = list(map(file["dataFunction"], data))
            except KeyError:
                # Do nothin cause there isn't a function to map
                pass

            print(f"Saving results for {file["name"]}")
            saveContentToCsv(file["name"], data)
        else:
            print(f"Error {response.status_code}")

    input("Press Enter to continue...")