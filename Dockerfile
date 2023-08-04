# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

FROM python:3.8
ADD app/ /
RUN pip install -r requirements.txt

EXPOSE 9000
CMD [ "python", "./helloworld_server.py"]