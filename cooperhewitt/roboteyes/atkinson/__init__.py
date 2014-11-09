import Image
import logging

def dither(src_path, dest_path, mime_type='GIF'):

    # Dithering in C because it is faster
    # https://github.com/migurski/atkinson
    
    try:
        try:
            return dither_atk(src_path, dest_path, mime_type)
        except Exception, e:
            logging.debug("dither using pure python")
            return dither_python(src_path, dest_path, mime_type)
        
    except Exception, e:
            
        # Sigh... things like: IOError: Unsupported BMP compression (1)
        
        logging.error("failed to dither %s: %s" % (src_path, e))
        return False

def dither_atk(src_path, dest_path, mime_type):

    import atk
    img = Image.open(src_path)
    img = img.convert('L')
    sz = img.size
    
    tmp = atk.atk(sz[0], sz[1], img.tostring())
    new = Image.fromstring('L', sz, tmp)
    
    new = img.convert('1')
    new.save(dest_path, mime_type)
    return True
    
def dither_python(src_path, dest_path, mime_type):

    img = Image.open(src_path)
    img = img.convert('L')
    
    threshold = 128*[0] + 128*[255]
    
    for y in range(img.size[1]):
        for x in range(img.size[0]):
            
            old = img.getpixel((x, y))
            new = threshold[old]
            err = (old - new) >> 3 # divide by 8
            
            img.putpixel((x, y), new)
            
            for nxy in [(x+1, y), (x+2, y), (x-1, y+1), (x, y+1), (x+1, y+1), (x, y+2)]:
                try:
                    img.putpixel(nxy, img.getpixel(nxy) + err)
                except IndexError:
                    pass

    img = img.convert('1')

    img.save(dest_path, mime_type)
    return True

if __name__ == '__main__':

    import sys

    source = sys.argv[1]
    dest = sys.argv[2]

    d = dither()
    d.dither(source, dest)

    sys.exit()
