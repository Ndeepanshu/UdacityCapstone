import os
SECRET_KEY = os.urandom(32)

# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

auth_config = {
    "AUTH0_DOMAIN"= 'dev-mx16muwc.auth0.com',
    "ALGORITHMS" = ['RS256'],
    "API_AUDIENCE" = 'Capstone'

}

bearer_tokens = {
    "casting_assistant" : "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkJMdTBfTFhfZlFHd0JXbW5rdjVrQyJ9.eyJpc3MiOiJodHRwczovL2Rldi1teDE2bXV3Yy5hdXRoMC5jb20vIiwic3ViIjoiZ29vZ2xlLW9hdXRoMnwxMTYyNDY4MzYzNzA2MzQzODk4MzEiLCJhdWQiOlsiQ2Fwc3RvbmUiLCJodHRwczovL2Rldi1teDE2bXV3Yy5hdXRoMC5jb20vdXNlcmluZm8iXSwiaWF0IjoxNTkwNjg0MDQ4LCJleHAiOjE1OTA3NzA0NDgsImF6cCI6IndyNFRCV25MM2dKcXFoVTBaQ0t1bFBza2szQmRRTERTIiwic2NvcGUiOiJvcGVuaWQgcHJvZmlsZSBlbWFpbCIsInBlcm1pc3Npb25zIjpbImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIl19.Hrwy2GLMCclbireQ2eh1-ZOvv3CcDWyz5CsYr5t-yQpPDOl75FQCqqkNsbPAPy58NiO0f7Xt2WCWMj5CovQNiYu594HUS1YWyRH_FsvQpMi129ck-5EqdCYZt-TGjbZlwJPwy1JUymR_kP7fxuIjZuosiXdk1NQ13ebDJnNzTdItHQgdlDQo0NsCV2kCRdWQWrpjhCVnHqA1ax8HagglvdQdG9UAsQk_2RZO0EB20KR6sHo_VxFnsPoJxDiyuRxwRE-WTif7C_P0OCrSvrI3TFXu7OZZfovRxHbqT9uXfHcxM_YHROpK0S4tgvQHqqLddymdzc3K0T4c9bYY_qBmxw",
    "casting_director" : "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkJMdTBfTFhfZlFHd0JXbW5rdjVrQyJ9.eyJpc3MiOiJodHRwczovL2Rldi1teDE2bXV3Yy5hdXRoMC5jb20vIiwic3ViIjoiZ29vZ2xlLW9hdXRoMnwxMTc1OTY5NDk0MjczMTMwOTk0NjciLCJhdWQiOlsiQ2Fwc3RvbmUiLCJodHRwczovL2Rldi1teDE2bXV3Yy5hdXRoMC5jb20vdXNlcmluZm8iXSwiaWF0IjoxNTkwNjg0NDMzLCJleHAiOjE1OTA3NzA4MzMsImF6cCI6IndyNFRCV25MM2dKcXFoVTBaQ0t1bFBza2szQmRRTERTIiwic2NvcGUiOiJvcGVuaWQgcHJvZmlsZSBlbWFpbCIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvciIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvciJdfQ.mAcqzS5DN3jVUTjVs2Hf7CJiWuSUjgkwov2VenphN7RnmEohmcwyhysLtYK5ODd8UwOzft2lgdyd-I_7Q9wi2OsrL8nfy8JtqWj8UdhMLEGVb9in7Op866Atz8gqXYAkKpxaC8twP5lapUhltN0aC7hEjnUjX6XhFlbL8yIOSH8aEGoymQkyl8x9liAD88PhFyU8EOx3P985qcBdDchxU5JAsr_R1Ixt-8n1313pHKs3mibKRULBVReAf9EI3ZPAl_MJ1VaOXV2_iJqGlC0lhf9wZwv3REFgkAHmqGDd4WnXoK2OPLoKHmyU8yhe9yWd-QKqSGWzomusZKsRC5QmPg"
    "executive_producer" : "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkJMdTBfTFhfZlFHd0JXbW5rdjVrQyJ9.eyJpc3MiOiJodHRwczovL2Rldi1teDE2bXV3Yy5hdXRoMC5jb20vIiwic3ViIjoiZ29vZ2xlLW9hdXRoMnwxMTg0MTM4OTkwNzc5Nzc3MTc4MTciLCJhdWQiOlsiQ2Fwc3RvbmUiLCJodHRwczovL2Rldi1teDE2bXV3Yy5hdXRoMC5jb20vdXNlcmluZm8iXSwiaWF0IjoxNTkwNjg0NjIyLCJleHAiOjE1OTA3NzEwMjIsImF6cCI6IndyNFRCV25MM2dKcXFoVTBaQ0t1bFBza2szQmRRTERTIiwic2NvcGUiOiJvcGVuaWQgcHJvZmlsZSBlbWFpbCIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvciIsImRlbGV0ZTptb3ZpZSIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvciIsInBvc3Q6bW92aWUiXX0.BDCzSIirLCU0SZ7nx_jxVp4xwfVfJPf_c8dWx-FEBEuLAYK0obkmbX8O9l6uM1tmV28h5TA01FnR26wnjpUOQzRgP8Auq7L0DaetX5g3W51KWgQwchZ9vEWRAA1MqMdzNRLf-w5Rb79iKMJPPih8K-pQQWRMZ-eraebgovGApbm3L6yXw571jo21Nf1ICQbSq_E5ieCOVnmpLfTffcN8tOlj_PBvCq5Dxay2JR4Ej7IQUcvTioJk0GLDyTYJ6ug1DOWX8kwxMSwrGt1r3AGjI2d1a5n0DDRFIo8kRPTnYJqPRPIzbH1QAw794i9qSwOeDbOfhg5MTyHgR1uXTbu7hA"
} 