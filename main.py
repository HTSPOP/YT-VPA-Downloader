from pytube import Playlist,YouTube
import os 
print("")

Hii =input("Hii I Am YT VPA Downloader Please Enter Your Name :- ")
print("")
print("HI",Hii)
print("")
Pass =input("Now Please Enter Your Password :- ")
print("")

if Pass == ("VPAD"):
    print ("OK Your Pass Word Is Correct Now You Can Prossed",Hii,)
    print("")

    W=input("Please Enter What You Have To Use Press \n (V For Video) \n (P For Playlist) \n (A For Audio) \n (Please Write Word IN Capital) :- ")
    print("")

else:
    print ("Try Again")   
    print("")

if W == ("V"):
    print("YOU Have Selected Video Download")
    print("")
    link = input("Enter YouTube video URL: ")
    print("")
    print("THANKS For Giving Link TO ME Now I Am Processing....")
    print("")
    def Download(link):
        youtubeObject = YouTube(link)
        youtubeObject = youtubeObject.streams.get_highest_resolution()
        try:
            print("YOur Video Has Downloading In Videos Folder That Is Created In Programes Folder")
            print("")
            youtubeObject.download(f"Youtube Videos Folder/")
        except:
            print("An error has occurred")
        print("Download is completed successfully")
        print("")

        print("OK NOW I AM SHUTDOWNDING THE VPA Downloader Bye Bye",Hii)
    Download(link)

elif W ==("P"):
    print ("YOU Have Selected Playlist Download")
    print("")

    playlist_url = input('Enter YouTube Playlist URL: ')
    print("")
    pl = Playlist(playlist_url)
    i=0
    print("THANKS For Giving Link TO ME Now I Am Processing....")
    print("")

    for video_url in pl.video_urls:
        i = i + 1
        try:
            yt = YouTube(video_url)
            video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
            video.download(f"YouTube Playlist Videos Folder/{yt.author}")

            print(f"Done !! {i} / {len(pl.video_urls)}")
            print("")
        
        except:
            print(f"Feld to download !! {i} / {len(pl.video_urls)}")
            print("")

            continue
        
    print('ALL DONE ')
    print("")
    
    print("OK NOW I AM SHUTDOWNDING THE VPA Downloader Bye Bye",Hii)
    print("")

elif W == ("A"):
    print ("You Have Selcted Audio Download")
    print("")
    print("Now Please Enter Link Below ")
    print("")
    yt = YouTube(str(input("Audio URL : "))) 
    print("")
    print("THANKS For Giving Link TO ME Now I Am Processing....")
    print("")
    video = yt.streams.filter(only_audio=True).first() 
    out_file = video.download(f"YouTube Audio Folder/{yt.author}") 
    base, ext = os.path.splitext(out_file) 
    new_file = base + '.mp3'
    os.rename(out_file, new_file) 
    print(yt.title + " has been successfully downloaded.")
    print("")
    
    print("OK NOW I AM SHUTDOWNDING THE VPA Downloader Bye Bye",Hii)
    print("")

else:
    print("Sorry You HAve Put Worng InPut SO I Am ShutDowning The VPA Downloader Sorry",Hii)
    print("")
    
    