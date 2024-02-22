import sys, re

# read file from std.in
#print output to std.out

#cabeçalhos 1 a 3 
# '(^#{1,3})\s(.*)\n'

#bold
# '\*\*(.*)\*\*'

#italic
# '\*(.*)\*'

#ordered lists
# '^(\d*?)\.(.*)\n'

#unordered lists
# '^- (.*)\n'

#links and images
# '(!)?\[(.+)\]\((\S+)\)'
#check if it's there    
def fix_regex(lines):
    first_list_item = True
    last_line_list_item = False

    for i in range(len(lines)-1):
        line = lines[i]
        

        cabecalho = re.match('(^#{1,3})\s(.*)\n',line)
        bold = re.match('\*\*(.*)\*\*',line)
        italic = re.match('\*(.*)\*',line)
        ord_list_item = re.match('^(\d*?)\.(.*)\n',line)
        unord_list_item = re.match('^- (.*)\n',line)
        links_images = re.match('(!)?\[(.+)\]\((\S+)\)',line)

        if(cabecalho != None):
            heading_size = len(cabecalho.group(1))
            lines[i] = f'<h{heading_size}>{cabecalho.group(2)}<\h{heading_size}>\n'

        if(bold != None):
            lines[i] = f'<b>{bold.group(1)}<\\b>'

        if(italic != None):
            lines[i] = f'<i>{italic.group(1)}<\\i>'

        if(ord_list_item or last_line_list_item or unord_list_item):
            if(first_list_item):
                first_list_item = False
                last_line_list_item = True
                
                if ord_list_item != None:
                    lines[i] = f'<ol>\n<li>{ord_list_item.group(2)}<\li>\n'
                else:
                    lines[i] = f'<ul>\n<li>{unord_list_item.group(1)}<\li>\n'

            elif ord_list_item:
                lines[i] = f'<li>{ord_list_item.group(2)}<\li>'
                last_line_list_item = True
            
            elif unord_list_item:
                lines[i] = f'<li>{unord_list_item.group(1)}<\li>'
                last_line_list_item = True

            elif last_line_list_item:
                last_line_list_item = False
                if str(lines[i]) == '\n':
                    if ord_list_item:
                        lines[i] = '<\ol>\n'
                    else:
                        lines[i] = '<\\ul>\n'
                first_list_item = True

        if(links_images != None):
            if(links_images.group(1) == '!'):
                lines[i] = f'<img src="{links_images.group(3)}" alt="{links_images.group(2)}"/>'        
            else:
                lines[i] = f'<a href="{links_images.group(3)}">{links_images.group(2)}</a>'        
    return lines

def main() -> None:
    lines = sys.stdin.readlines()
    if lines != None:
        new_lines = fix_regex(lines)
        new_lines = ''.join(new_lines)
        print(new_lines)
    return

if __name__ == '__main__':
    main()