import time,pygame,threading
curnt_time=time.strftime("%H:%M:%S")
work_start="09:00:00"
work_end="17:00:00"
def ex():
    time.sleep(13)
    while work_start<curnt_time<work_end:
        pygame.mixer.init()
        pygame.mixer.music.load("TrackA.mp3")
        pygame.mixer.music.play()
        A=None
        while True:
            print("\n","Please do exercise")
            A = input("if u have done ex enter done to stop music = ").capitalize()
            if A=="Done":
                pygame.mixer.music.stop()
                with open("logs of Exercises","a") as f:
                    f.write("Exercise done at "+time.strftime("%H:%M:%S")+"\n")

                break

        time.sleep(36)
def wt():
    while work_start<curnt_time<work_end:

        pygame.mixer.init()
        pygame.mixer.music.load("2013-10-20_Preparation_2_-_David_Fesliyan.mp3.pbanu2x.partial")
        pygame.mixer.music.play()
        A=None
        while True:
            print("\n","Please drink water")
            A = input("if u have drink water enter done to stop music = ").capitalize()
            if A=="Done":
                pygame.mixer.music.stop()
                with open("logs of water","a") as f:
                    f.write("water done at "+time.strftime("%H:%M:%S")+"\n")

            break

        time.sleep(60)
t1=threading.Thread(target=ex)
t2=threading.Thread(target=wt)
t1.start()
t2.start()