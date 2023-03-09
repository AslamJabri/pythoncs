def main():
    extension = input("File name: ")
    print(dec(extension))
    
def dec(n):
    if n.endswith(".gif"):
        return "image/gif"
    elif n.endswith(".jpg") or n.endswith(".jpeg"):
        return "image/jpeg"
    elif n.endswith(".png"):
        return "image/png"
    elif n.endswith(".pdf"):
        return "application/pdf"
    elif n.endswith(".zip"):
        return "application/zip"
    elif n.endswith(".txt"):
        return "text/plain"
    else:
        return "application/octet-stream"
        
        
        
main()