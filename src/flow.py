from prefect import flow


@flow
def beep():
    print("boop")


beep()
