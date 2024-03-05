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
            "name": "",
            "query": """""",
            "dataFunction": lambda example: example*2
        },
    ]
    apiKey = ''

    for file in files:
        print(f"Calling the API for {file["name"]}")
        response = requests.post(
            '',
            headers={
                "api-key": apiKey,
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