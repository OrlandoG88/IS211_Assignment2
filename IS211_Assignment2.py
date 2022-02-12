import argparse
import urllib.request
import logging
import datetime



def downloadData(url):
    with urllib.request.urlopen(url) as response:
        web_data = response.read().decode('utf-8')

    return web_data


def processData(filecontent):
    person_dict = {}
    for data_line in filecontent.split("\n"):
        if len(data_line) == 0:
            continue

        identifier, name, birthday = data_line.split(",")
        if identifier == "id":
            continue

        id_int = int(identifier)
        try:
            real_birthday = datetime.datetime.strptime(birthday, "%d/%m/%Y")
            person_dict[id_int] = (name, real_birthday)
        except ValueError as e:
            error_msg = "Error processing line #{} for ID #{}.".format(id, id)
            logging.basicConfig(filename="error.log", level=logging.ERROR)
            logger = logging.getLogger("assignment2")
            logger.error(error_msg)




    return person_dict


def displayPerson(id, personData):
    if id in personData:
        name = personData[id][0]
        birthdate = datetime.datetime.strftime(personData[id][1], "%Y-%m-%d")
        print(f"Person {id} is {name} and real birthday is {birthdate}")
    else:
        print ("No user found with that ID")




def main(url):
    print(f"Running main with URL = {url}...")
    data = downloadData(url)
    results_dict = processData(data)



    while True:
        id = int(input("Enter ID to lookup: "))
        if id <= 0:
           break
        else:
           displayPerson(id, results_dict)











if __name__ == "__main__":
    """Main entry point"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", help="URL to the datafile", type=str, required=True)
    args = parser.parse_args()
    main(args.url)









