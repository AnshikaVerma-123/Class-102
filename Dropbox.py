def upload_file (img_name):
    access_token = ""
    file = img_counter
    file_from = file
    file_to = "/newFolder1/" + (img_name)
    dbx = dropbox.Dropbox (access_token)
    