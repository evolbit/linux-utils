import glob

"""
Some linux desktop environments do not provide choosing a slideshow 
(set of images in sequence) in an easy way. This little script can
help in this situation generating a XML that can be used as Wallpaper.
It uses all the images that belong to a given path.
"""

def generate_slideshow(directory, dur_img, dur_trans):
    if directory[-1] == '/':
        directory = directory[:-1]
        
    lst = glob.glob(directory+'/*.jpg')

    string = '<background>\n\
                \t<starttime>\n\
                    \t\t<year>2015</year>\n\
                    \t\t<month>01</month>\n\
                    \t\t<day>01</day>\n\
                    \t\t<hour>00</hour>\n\
                    \t\t<minute>00</minute>\n\
                    \t\t<second>00</second>\n\
                \t</starttime>\n'

    for i in range(len(lst)):

        if i == (len(lst) - 1):
            j = 0
        else:
            j = i + 1
            
        static = '\t<static>\n\
                  \t\t<duration>' + str(dur_img) + '</duration>\n\
                  \t\t<file>' + lst[i] + '</file>\n\
                  \t</static>\n\n'

        transition = '\t<transition>\n\
                      \t\t<duration>' + str(dur_trans) + '</duration>\n\
                      \t\t<from>' + lst[i] + '</from>\n\
                      \t\t<to>' + lst[j] + '</to>\n\
                      \t</transition>\n\n\n'
        
        string = string + static + transition

    string = string + '</background>\n'

    file = open(directory+'/slideshow.xml','w')
    file.write(string)
    file.close()
    print('XML written to ' + directory+'\nHave Fun!\n')
