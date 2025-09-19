with open('current_time.py','r') as f:
    content = f.readlines()

reversed_lines = [line.strip()[::-1]for line in content]

with open('reverse_text.txt','w') as f:
    for line in reversed_lines:
        f.write(line + '\n') 

print("file reversed successfully and stored in reverse_text.txt file")