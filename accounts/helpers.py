
def success(message="Success Message",data={},status=200):
    return {
        "status":status,
        "success":True,
        "message":message,
        "data":data
    }

def failure(message="Failure Message",status=400):
    return {
        "status":status,
        "success":False,
        "message":message
    }
