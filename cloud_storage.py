import dropbox

class TransferData:
   def _init_(self,access_token):
          self.access_token = access_token

   def upload_file(self,file_from,file_to):
       dbx = dropbox.Dropbox(self.access_token)

      
       f=open(file_from,'rb')    
       dbx.files_upload(f.read(),file_to)


   def main():
     access_token = 'sl.A-1x9os-sUiadWkvBI_5qb9IhDkqt2PZIkTQJrFdE9ddBktbEEa6BaM6t1wGEdLjZDLGjR2ofR8Tv9HLe5rumqa_fCPX6J3-fj0RNgIr10MN_MNX5DzuSeWUWAyAC0DYCQk8MFk'
     transferData = TransferData(access_token)

     file_from = input("Enter the file path to transfer :-")
     file_to = input("enter the full path to upload to dropbox:-") 

     # API v2
     transferData.upload_file(file_from,file_to)
     print("file has been moved !!!")



main()         