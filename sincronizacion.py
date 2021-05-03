from google.cloud import storage
import os
from os import listdir
from os.path import isfile, isdir



os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="C:/Users/Simio/Desktop/Nueva carpeta/pythonprobe-firebase-adminsdk-58ruy-2450f44600.json"



def upload_blob(bucket_name, source_file_name, destination_blob_name):
        """Uploads a file to the bucket."""
        # bucket_name = "your-bucket-name"
        # source_file_name = "local/path/to/file"
        # destination_blob_name = "storage-object-name"

        
        bucket = storage_client.bucket(bucket_name)
        blob = bucket.blob(destination_blob_name)
        blob.upload_from_filename(source_file_name)

        print(
            "File {} uploaded to {}.".format(
                source_file_name, destination_blob_name
            )
        )

def list_blobs(bucket_name):
        """Lists all the blobs in the bucket."""
        # bucket_name = "your-bucket-name"
        blobslist = []

        storage_client = storage.Client()

        # Note: Client.list_blobs requires at least package version 1.17.0.
        blobs = storage_client.list_blobs(bucket_name)

        for blob in blobs:
        	blobslist.append(blob.name)
        
        return blobslist


def list_blobs_with_prefix(bucket_name, prefix, delimiter=None):

    storage_client = storage.Client()

    blobs = storage_client.list_blobs(
        bucket_name, prefix=prefix, delimiter=delimiter
    )

    print("Blobs:")
    for blob in blobs:
        print(blob.name)

    if delimiter:
        print("Prefixes:")
        for prefix in blobs.prefixes:
            print(prefix)


def download_blob(bucket_name, source_blob_name, destination_file_name):
        """Downloads a blob from the bucket."""
        # bucket_name = "your-bucket-name"
        # source_blob_name = "storage-object-name"
        # destination_file_name = "local/path/to/file"

        bucket = storage_client.bucket(bucket_name)
        blob = bucket.blob(source_blob_name)
        try:
            blob.download_to_filename(destination_file_name)
        except: print("F")

        print(
            "Blob {} downloaded to {}.".format(
                source_blob_name, destination_file_name
            )
        )

def ls1(path):    
     return [obj for obj in listdir(path) if isfile(path + obj)]


def upcomparation(folderlist, cloudlist):
	uplist = []
	
	comparation = "false"

	for compare1 in folderlist:

		for compare2 in cloudlist:
			if compare1 == compare2:
				comparation = "true"
				break
			else:
				comparation = "false"

		if comparation == "false":
			uplist.append(compare1)

	return uplist

def downcomparation(folderlist, cloudlist):
	downlist = []

	comparation = "false"

	for compare2 in cloudlist:
		for compare1 in folderlist:
			if compare1 == compare2:
				comparation = "true"
				break
			else:
				comparation = "false"

		if comparation == "false":
			downlist.append(compare2)



	return downlist


def sync(uplist, downlist, bucket_name, source_file_name_, destination_file_name_):


	for updoc in uplist:
		source_file_name = source_file_name_ + updoc
		destination_blob_name = updoc
		upload_blob(bucket_name, source_file_name, destination_blob_name)

	print("archivos cargados...nube actualizada")


	for downdoc in downlist:
		destination_file_name = destination_file_name_ + downdoc
		source_blob_name = downdoc
		download_blob(bucket_name, source_blob_name, destination_file_name)


	print("archivos descargados...carpeta actualizada")


#___________________________________________________________________________________________________________________________________________________________

#escribir entre las comillas la direccion de la carpeta a sincronizar

source_file_name_ ="C:/Users/Simio/Desktop/Nueva carpeta/Nueva carpeta/"

#___________________________________________________________________________________________________________________________________________________________


storage_client = storage.Client()
bucket_name="pythonprobe.appspot.com"
#destination_blob_name = "one/he"
prefix=None
delimiter=None

#source_blob_name = "one/heart"
destination_file_name_ = source_file_name_
path = destination_file_name_


folderlist = ls1(path)
cloudlist = list_blobs(bucket_name)

print ("lista foler: ",folderlist)
print ("lista cloud: ",cloudlist)
uplist = upcomparation(folderlist, cloudlist)
downlist = downcomparation(folderlist, cloudlist)

print("subir: ",uplist)
print("descargar: ",downlist)

sync(uplist, downlist, bucket_name, source_file_name_, destination_file_name_)

uplist = upcomparation(folderlist, cloudlist)
downlist = downcomparation(folderlist, cloudlist)

print("subir: ",uplist)
print("descargar: ",downlist)


folderlist = ls1(path)
cloudlist = list_blobs(bucket_name)

print ("lista foler: ",folderlist)
print ("lista cloud: ",cloudlist)
