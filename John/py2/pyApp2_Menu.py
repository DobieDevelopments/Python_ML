import sys, os, os.path, cv2, numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
from PIL import Image
#plt.rcParams["figure.figsize"] = 100,100

path = os.getcwd() +"\\test_images"

ROOT_PATH = "N:\\Sunfl\\Downloads"
train_data_directory = os.path.join(ROOT_PATH, "train_images")
test_data_directory = os.path.join(ROOT_PATH, "small_test_data") #"test_images")

def main_menu():
    """Prints a main menu to screen"""
    print("hello")
    os.system('cls') # cls in windows, clear in linux
    print("-----------------------------")
    print("Main Menu")
    print("-----------------------------")
    print("hi")
    print("Press 1 to go to do a thing")
    execute()
    #menu_action(input())
    return

def menu_action(selection):
    if selection == '1':
            execute()
    return

def execute():
    images = load_data(test_data_directory)
    print(images[0])

    #doggos = [200, 139, 864, 40]
    #for i in range(len(doggos)):
    #    plt.subplot(1, 4, i+1)
    #    plt.axis('off')
    #    plt.imshow(images[doggos[i]])
    #    plt.subplots_adjust(wspace=0.5)

    #plt.show()

    #print("shape: {0}, min: {1}, max: {2}".format(images[doggos[i]].shape, 
    #                                              images[doggos[i]].min(), 
    #                                              images[doggos[i]].max()))

    plt.figure(figsize=(100,100))
    
    i = 1
    for image in images:
        plt.subplot(10,100,i)
        plt.axis('off')
        #plt.title("Label {0} ({1})".format("doggo #", i))
        #image = cv2.resize(image, dsize=(480, 350), interpolation = cv2.INTER_CUBIC)
        #image = tf.reshape(image,[-1, 350, 480, 1])
        #depth = image.shape[-1]
        #assert depth == 3 or depth == 1
        #if depth == 1:
        image = np.expand_dims(image, axis=3)
        image = tf.image.grayscale_to_rgb(image)
        image = tf.cast(image, tf.uint8)
        #plt.imshow(image)
        #cv2.imwrite("test_save/"+ i + ".jpg", image)
        write_data(i, image, test_data_directory)
        i+= 1
        if i > 50:
            break

    #plt.show()
    return

def write_data(i, image, data_directory):
    file_names = [os.path.join(data_directory, f)
        for f in os.listdir(data_directory)
            if f.endswith(".jpg")]

    print(i)
        #image = cv2.resize(image, (480, 350), interpolation=cv2.INTER_CUBIC)
    graph = tf.Graph()
    with graph.as_default():
        im = tf.placeholder(tf.uint8)
        op = tf.image.encode_jpeg(im, format='rgb', quality=100)
        init = tf.initialize_all_variables()
    
        image = image[:,:,0,:]
        tf.image.encode_png(image)
        tf.write_file(path+"test_save/"+ str(i) + ".jpg", 'image')
    
    with tf.Session(graph=graph) as sess:
        sess.run(init)
        data_np = sess.run(op, feed_dict={ im: image })

    with open(filepath, 'w') as fd:
        fd.write(data_np)
        #image.save("test_save/"+ f + ".jpg")
        #cv2.imwrite("test_save/"+ f + ".jpg", image)
    return

def load_data(data_directory):
    #directories = [d for d in os.listdir(data_directory) 
    #               if os.path.isdir(os.path.join(data_directory, d))]
    labels = []
    images = []
    #for d in directories:
        #label_directory = os.path.join(data_directory, d)
    file_names = [os.path.join(data_directory, f) 
    for f in os.listdir(data_directory) 
        if f.endswith(".jpg")]
    for f in file_names:
        images.append( Image.open(f)) #cv2.imread(f, -1))

        #images = np.asarray(images)
        #images = np.expand_dims(images, axis=3)
        print(f)
    return images

def execute_menu_action(selection):
    """Handles input and executes the desired menu item"""
    if selection == '1':
        print("-----------------------------")
        print("Menu 1")
        print("-----------------------------")
        print("Press 1 to go back")
        print("Press 2 to go to menu 2")
        print("Press 3 to import images")
        print("Press anything else to quit.")
        i = input()
        if i == '1':
            main_menu()
        if i == '2':
            execute_menu_action('2')
        if i == '3':
            loadImages()
            main_menu()
        if i == '4':
            sys.exit
    elif selection == '2':
        print("-----------------------------")
        print("Menu 2")
        print("-----------------------------")
        print("Press 1 to go back")
        print("Press 2 to go to menu 1")
        print("Press anything else to quit.")
        i = input()
        if i == '1':
            main_menu()
        if i == '2':
            execute_menu_action('1')
    else:
        main_menu()
    return

#https://www.datacamp.com/community/tutorials/tensorflow-tutorial
def loadImages():
    if not os.path.exists("test_save"):
        os.mkdir("test_save")
  #  imgs = []
    valid_types = [".jpg",".gif",".png",".tga"]
    for f in os.listdir(path):
        print(path + "/" + f)
        ext = os.path.splitext(f)[1]
        if ext.lower() not in valid_types:
            continue
   #     imgs.append(cv2.imread(path+"/"+f))
        load = cv2.imread(path+"/"+f)
        load = cv2.resize(load, dsize=(480, 350), interpolation = cv2.INTER_CUBIC)
        np_image_data = numpy.asarray(load)
        load = tf.expand_dims(load, -1)
        image = tf.image.grayscale_to_rgb(load)
        image = cv2.resize(load, dsize=(480, 350), interpolation = cv2.INTER_CUBIC)
        cv2.imwrite("test_save/"+f, image)
        #if len(imgs) > 500:
         #   for i in imgs:
          #      print(i)
                #with open("test_save", "w") as folder:
                #x = Image.open(i, "BMP") 
           #     Image.SAVE("test_save/"+ i + ".jpg", format="JPG")
            #imgs = []
    return

#Run main program
if __name__ == "__main__":
    main_menu()
    sys.exit    # sys.exit(0) raises a SystemExit exception traceback