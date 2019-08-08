import gkeepapi  # importing the unofficial api. google hasn't released an offical api for keep

with open("the file path which you want to open") as file # opening the file from your local storage
  keep = gkeepapi.Keep()  # creating object
  keep.login('username', 'password')  # login
  gnote = keep.get('note id. can find it in the url')  # getting the note
  gnote.text = file.read()  # reading the locally stored file and transmiting it to the keep note
print(gnote.text)  #printing just to make sure. can comment it out after testing
keep.sync()  #finally, syncing the file. Done.
