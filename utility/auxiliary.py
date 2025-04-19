import os
# This return the maximum and minimum date of the existing/historical data
def get_current_file(client,bucket_name):

    # list out all the files in the bucket
    objects = client.list_objects(bucket_name,recursive=True)

    # Extract the file names
    file_names = [ os.path.basename(obj.object_name).split('.')[0] for obj in objects]

    # convert file name to a tuple (year,month)
    parsed_elements = [tuple(map(int,item.split('-'))) for item in file_names]

    # Return min and max (Year, month)
    if not parsed_elements or not parsed_elements:
        return ([],[])
    return min(parsed_elements),max(parsed_elements)