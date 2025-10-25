import re
from .parser_generic import MedicalDocParser

class PatientDetailsParser(MedicalDocParser):
    def __init__(self, text):
        MedicalDocParser.__init__(self, text)

    def parse(self):
        return{
            "patient_name": self.get_field("patient_name"),
            "phone_no": self.get_field("phone_no"),
            "vaccination_status": self.get_field("vaccination_status"),
            "medical_problems": self.get_field("medical_problems"),
            "has_insurance": self.get_field("has_insurance")
        }
    
    def get_field(self, field_name):
        pattern_dict = {
            "patient_name": {"pattern": "Date\n+([a-zA-Z]+\s+[a-zA-Z]+).\D{3}"},
            "phone_no": {"pattern": "(\(\d{3}\).\d{3}.\d{4}).+Weight"},
            "vaccination_status": {"pattern": "vaccination\?\n+(Yes|No)"},
            "medical_problems": {"pattern": "headaches\):\n+(\D+?)\n"},
            "has_insurance": {"pattern": "insurance\?\n+(Yes|No)"}
        }

        pattern_object = pattern_dict.get(field_name)
        if pattern_object:
            matches = re.findall(pattern_object["pattern"], self.text)
            if len(matches) > 0:
                return matches[0].strip()
            
        

