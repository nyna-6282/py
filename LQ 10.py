def copy_alt_lines(file1,file2):
    try:
        with open(file1,'r') as f1,open(file2,'w') as f2:
            for line_no ,line in enumerate(f1,start=1):
                if line_no%2!=0:
                    f2.write(line)
            print("ALETRNATE (ODD_NUMBERED) LINES COPIED FROM ",file1," to ",file2)
    except FileNotFoundError:
        print("ERROR : THE FILE ",file1,"DOES NOT EXIST ")
copy_alt_lines('file1.txt','file2.txt')
