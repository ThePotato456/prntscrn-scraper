import os
import json
import re


file_info = []
btc_addresses = []
for image in os.listdir('./image_text/'):
    with open(f'./image_text/{image}', 'r') as file:
        text = ''
        for line in file.readlines():
            
            reg = r'([13]|bc1)[A-HJ-NP-Za-km-z1-9]{27,34}'
            if re.match(reg, line):
                btc_addresses.append(line)

            text = text + line

        file_info.append({'img_path': f'./images/{image}', 'img_text_path': f'./image_text/{image}', 'text': text})

with open('json_output.json', 'w+') as json_output:
    json_output.write(json.dumps(file_info, indent=2))

print(json.dumps(btc_addresses, indent=2))