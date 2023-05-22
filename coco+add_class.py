import os
import shutil


def create_foder(lst):
    for i in lst:
        if os.path.exists(i):
            shutil.rmtree(i)
        os.makedirs(i)
    print('save_foder is created!')
    

def init(source_list,save_list):
    # 检查待转换的数据是否存在
    for path in source_list:
        if (os.path.exists(path)):
            print('find data foder: ',path)

        else:
            print('not find data foder: ',path,'\n')
            return False
        
    num_data=0
    for path_save in save_list:
        if (os.path.exists(path_save)):
            num_data += len(os.listdir(path_save))

    if(num_data > 0):
        print('save_list alrady exists,Delete and Recreate?')
        result = input('enter y or n:\t')
        if (result =='y' or result=='Y'):
            create_foder(save_list)

            
        elif (result == 'n' or result=='N'):
            exit(0)
        
        else:
            exit(0)
    elif(num_data == 0):
        create_foder(save_list)

def convert(source_list,save_list):
    val_data =      [source_list[0],source_list[1],save_list[0],save_list[1]]
    train_data =    [source_list[2],source_list[3],save_list[2],save_list[3]]

    for data in [val_data,train_data]:

        print('coverting:\n'+data[2]+'\n'+data[3])

        lst = os.listdir(data[0])
        for i in lst:
            has_copy = False

            with open(os.path.join(data[0],i),'r') as f:
                txts = f.readlines()
                for txt in txts:
                    
                    info = txt.split(' ')
                    if (info[0] in label_class.values()):

                        if (not has_copy):
                            shutil.copy(os.path.join(data[1],i.split('.')[0]+'.jpg'), os.path.join(data[3],i.split('.')[0]+'.jpg'))
                            has_copy = True
            
                        with open(os.path.join(data[2],i),'a') as f_lab: 

                            if (info[0] == "56"): #56:chair 修改为0
                                cls = list(label_class.values()).index('56')                           
                                new_txt = ' '.join((str(cls),info[1],info[2],info[3],info[4]))
                                f_lab.write(new_txt)

                            elif(info[0] == "41"):   #41:cup 修改为1
                                cls = list(label_class.values()).index('41')
                                new_txt = ' '.join(('1',info[1],info[2],info[3],info[4]))
                                f_lab.write(new_txt)
                                
                            elif(info[0] == "66"): #66:keyboard 修改为2
                                cls = list(label_class.values()).index('66')
                                new_txt = ' '.join(('2',info[1],info[2],info[3],info[4]))
                                f_lab.write(new_txt)

                            elif(info[0] == "0"): #66:person 修改为3
                                cls = list(label_class.values()).index('0')
                                new_txt = ' '.join(('3',info[1],info[2],info[3],info[4]))
                                f_lab.write(new_txt)

                            # 增加类别即可

        print('*'*20+"done"+'*'*20)

if __name__ == "__main__":
    # old_index为所要提取的类别在原始coco数据集中的编号
    # 提取后新的编号为label_class的类别放置的顺序号

    label_class =   {
                    "chair":       '56',  #[class name, old_index]
                    "cup":         '41',
                    "keyboard":    '66',
                    "person":      '0',
                    }
    # coco数据集下载地址:
    # 浏览器下载会中断，强烈建议使用迅雷等PT下载工具
    # images_train_foder =  'http://images.cocodataset.org/zips/train2017.zip',  # 19G, 118k images
    # images_val_foder =    'http://images.cocodataset.org/zips/val2017.zip',  # 1G, 5k images

    # labels_train_foder =  'https://github.com/ultralytics/yolov5/releases/download/v1.0/coco2017labels.zip'  # labels
    # labels_val_foder =    'https://github.com/ultralytics/yolov5/releases/download/v1.0/coco2017labels.zip'  # labels

    # 验证集标签文件夹
    labels_val_foder =      r"D:\迅雷下载\coco2017labels\coco\labels\val2017"
    # 验证集图片文件夹
    images_val_foder =      r"D:\迅雷下载\val2017\val2017"
    # 训练集标签文件夹
    labels_train_foder =    r"D:\迅雷下载\coco2017labels\coco\labels\train2017"
    # 训练集标签文件夹
    images_train_foder =    r"D:\迅雷下载\train2017\train2017"
    # 处理后的验证集标签存储文件夹
    labels_val_foder_save =     r"D:\DL\datasets\coco_4\labels\val"
    # 处理后的验证集图片存储文件夹
    images_val_foder_save =     r"D:\DL\datasets\coco_4\images\val"
    # 处理后的训练集标签存储文件夹
    labels_train_foder_save =   r"D:\DL\datasets\coco_4\labels\train"
    # 处理后的训练集图片存储文件夹
    images_train_foder_save =   r"D:\DL\datasets\coco_4\images\train"

    data_foder =        [
                        labels_val_foder,
                        images_val_foder,
                        labels_train_foder,
                        images_train_foder
                        ]
    
    data_foder_save =   [
                        labels_val_foder_save,
                        images_val_foder_save,
                        labels_train_foder_save,
                        images_train_foder_save
                        ]
    
    init(data_foder,data_foder_save)

    convert(data_foder,data_foder_save)
