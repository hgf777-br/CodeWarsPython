import re
import statistics

def stat(strg):
    strg = strg.split()
    team = []
    data = {}
    result= ""
    
    for x in strg:
        crono = re.findall(r"[0-9]+", x)
        team.append(int(crono[0])*3600 + int(crono[1])*60 + int(crono[2]))
    
    data['Range'] = (max(team) - min(team))
    data['Average'] = (statistics.mean(team))
    data['Median'] = (statistics.median(team))
    
    for x,y in zip(data.keys(), data.values()):
        h = y / 3600
        m = (h - int(h)) * 60
        s = (m - int(m)) * 60
        result += x + ": " + r"{:02d}|{:02d}|{:02d} ".format(int(h), int(m), int(s))

    return result[:-1]
    
teste = "01|15|59, 1|47|16, 01|17|20, 1|32|34, 2|17|17"

print(stat(teste))