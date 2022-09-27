import sys
import json
import logging
from rich.progress import track
from qcloud_cos import CosConfig, CosS3Client

with open("./config.json", "r", encoding = "utf-8") as f:
    config = json.load(f)

logging.basicConfig(level = logging.ERROR, stream = sys.stdout)
config = CosConfig(
    SecretId = config["secretId"],
    SecretKey = config["secretKey"],
    Token = None,
    Scheme = "https",
    Region = config["region"]
)

client = CosS3Client(config)
failedFiles = []

marker = ""
while True:
    response = client.list_objects(
        Bucket = config["bucket"],
        Prefix = config["folder"],
        Marker = marker
    )
    for file in track(response["Contents"]):
        try:
            downloadResponse = client.download_file(
                Bucket = config["bucket"],
                Key = file["Key"],
                DestFilePath = "./" + file["Key"]
            )
        except:
            failedFiles.append(file)
    if response["IsTruncated"] == "false":
        # Don't ask me why "false", ask qcloud heh
        break
    marker = response["NextMarker"]

with open("./failed.json", "w", encoding = "utf-8") as f:
    json.dump(failedFiles, f, ensure_ascii = False, indent = 4)
