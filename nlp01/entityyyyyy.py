import re
def extract_entities(text):
    entities=[]
    date_pattern=r'\d{2}/\d{2}/\d{2,4}'
    number_pattern=r'\d+'
    name_pattern=r'[A-Z][a-z]+'
    dates=re.findall(date_pattern,text)
    entities.extend([('DATE',date) for date in dates])
    numbers=re.findall(number_pattern,text)
    entities.extend([('NUMBER',number) for number in numbers])
    names=re.findall(name_pattern,text)
    entities.extend([('NAME',name) for name in names])
    return entities
if __name__=="__main__":
    text="I Was Born On 01/06/2004 In Tirupathi"
    entities=extract_entities(text)
    if entities:
        print("entities found")
        for entity_type,entity_value in entities:
            print(f"{entity_type}:{entity_value}")
    else:
        print("no entities found")

