#!/usr/local/bin/pyton

import shellui
import pprint
from collections import OrderedDict

''' Testing Constants'''
LIST_DICTS = [
{"name": "Tom", "age": 10, "ethnicity":"Caucasion"},
{"name": "Mark", "age": 5, "ethnicity":"Asian"},
{"name": "Pam", "age": 7, "ethnicity":"Hispanic"}
]

LIST_OF_DICTS = [{'Gears': '60', 'MaxActvGears': '30', 'hostname': 'lae-rtp1-lx-60'},
                 {'Gears': '50', 'MaxActvGears': '30', 'hostname': 'lae-rtp1-lx-50'},
                 {'Gears': '40', 'MaxActvGears': '30', 'hostname': 'lae-rtp1-lx-40'},
                 {'Gears': '30', 'MaxActvGears': '30', 'hostname': 'lae-rtp1-lx-30'},
                 {'Gears': '20', 'MaxActvGears': '30', 'hostname': 'lae-rtp1-20'},
                 {'Gears': '10', 'MaxActvGears': '30', 'hostname': 'lae-rtp1-10'},
                 {'Gears': '00', 'MaxActvGears': '30', 'hostname': 'lae-rtp1-00'}]

if __name__ == "__main__":
    shutil = shellui.ShellUI()

    shutil.logging_create(filename='log_one.log', filemode='a', level=20,
                               format='%(asctime)s %(levelname)s:%(filename)s: %(message)s',)

    for dictionary in LIST_OF_DICTS:
        if int(dictionary["Gears"]) == 00:
            shutil.logmsg(20, "The following host is fine: {}".format(dictionary['hostname']))
        elif int(dictionary["Gears"]) == 10:
            shutil.logdebug("You might want debug this host: {}".format(dictionary['hostname']))
        elif int(dictionary["Gears"]) == 20:
            shutil.loginfo("Information provided for host: {}".format(dictionary['hostname']))
        elif int(dictionary["Gears"]) == 30:
            shutil.logwarning("Approacing Maximum Amount of Gears: {}".format(dictionary['hostname']))
        elif int(dictionary["Gears"]) == 40:
            shutil.logerror("There is an error with host: {}".format(dictionary['hostname']))
        elif int(dictionary["Gears"]) == 50:
            shutil.logcritical("Exceeded Maximum Amount of Gears: {}".format(dictionary['hostname']))

    for dictionary in LIST_OF_DICTS:
        if int(dictionary["Gears"]) == 00:
            shutil.logging_enable()
            shutil.logmsg(20, "The following host is fine: {}".format(dictionary['hostname']))
        elif int(dictionary["Gears"]) == 10:
            shutil.logdebug("You might want debug this host: {}".format(dictionary['hostname']))
        elif int(dictionary["Gears"]) == 20:
            shutil.logging_disable()
            shutil.loginfo("Information provided for host: {}".format(dictionary['hostname']))
        elif int(dictionary["Gears"]) == 30:
            shutil.logwarning("Approacing Maximum Amount of Gears: {}".format(dictionary['hostname']))
        elif int(dictionary["Gears"]) == 40:
            shutil.logerror("There is an error with host: {}".format(dictionary['hostname']))
        elif int(dictionary["Gears"]) == 50:
            shutil.logcritical("Exceeded Maximum Amount of Gears: {}".format(dictionary['hostname']))
    
    shutil.logging_disable()

    json_dicts = shutil.import_json('./sample_json.json')
    shutil.export_json('./output_json.json', LIST_DICTS)

    #Testing Ordered Dict to Dict operation
    ordered_dict = OrderedDict([("name", "Uni"), ("age", 129), ("ethnicity", "Mars Citizen")])
    print type(ordered_dict)
    pprint.pprint(ordered_dict)
    for item in ordered_dict:
        print item

    LIST_DICTS.append(ordered_dict)

    csv_dicts = shutil.import_csv('./sample_csv.csv')
    shutil.export_csv('./output_csv.csv', LIST_DICTS)

    tsv_dicts = shutil.import_csv('./sample_tsv.tsv')
    shutil.export_csv('./output_tsv.tsv', LIST_DICTS, delimiter='\t')

    tsv_dicts = shutil.import_csv('./sample_tsv.tsv')
    shutil.export_csv('./output_tsv_h.tsv', LIST_DICTS, delimiter='\t', header=['name','age','ethnicity'])

    xml_dicts = shutil.import_xml('./sample_xml.xml')
    shutil.export_xml('./output_xml.xml', LIST_DICTS)

    print shutil.scriptpath()


