import numpy as np
import glob
import os


def get_range_min_max_of_depth(depth_arr,file_id):
    depth_min=depth_arr.min()
    depth_max=depth_arr.max()
    depth_range=depth_arr.max()-depth_arr.min()
    print(f'[No {file_id}]')
    print('Depth min:',depth_min)
    print('Depth max:',depth_max)
    print('Depth range:',depth_range)
    print('===============================')

    return {
        "depth_range":depth_range,
        "depth_max":depth_max,
        "depth_min":depth_min
    }


def scale_shift_depth(depth_arr,scale_factor=297,shift_factor=0.824):
    new_depth_arr=depth_arr * scale_factor + shift_factor
    return new_depth_arr

if __name__=="__main__":

    ## get the range of the depth
    '''
    depth_range=[]
    depth_min=[]
    depth_max=[]

    depth_file_list=['100027','100030','100033','100035','100040']  
    for file_id in depth_file_list:
        file_path=f'out_rgb_img_nyu/out_{file_id}.txt'
        depth_arr=np.loadtxt(file_path)
        depth_stat=get_range_min_max_of_depth(depth_arr,file_id)
        depth_range.append(depth_stat['depth_range'])
        depth_min.append(depth_stat['depth_min'])
        depth_max.append(depth_stat['depth_max'])
    
    print('Mean stat')
    print('mean range:',sum(depth_range)/len(depth_range))
    print('mean max:',sum(depth_max)/len(depth_max))
    print('mean min:',sum(depth_min)/len(depth_min))
    print('===============================')
    '''

    '''
    depth_txt_folder_dir = '/home/gp3/Desktop/wild_gan/LapDepth-release/out_img_align_celeba_test'
    depth_txt_list = sorted(glob.glob(depth_txt_folder_dir + '/*.txt'))
    done_depth_txt_list=glob.glob(depth_txt_folder_dir + '/*new.txt')
    no_new_depth_txt_list=list(set(depth_txt_list)-set(done_depth_txt_list))
    done_depth_txt_ori_list=[]
    for i in range(len(done_depth_txt_list)):
        done_depth_txt_ori_list.append(done_depth_txt_list[i].replace('_new.txt','.txt'))
    no_done_depth_txt_list=list(set(no_new_depth_txt_list)-set(done_depth_txt_ori_list))
    no_done_depth_txt_list=sorted(no_done_depth_txt_list)
    '''

    ## shift and scale the depth
    '''
    for i in range(len(no_done_depth_txt_list)):
        if i >= 0 and i <=20000:
            depth_txt_path=no_done_depth_txt_list[i]
            print(f'Process {depth_txt_path}')
            depth_arr=np.loadtxt(depth_txt_path)
            new_depth_arr=scale_shift_depth(depth_arr,scale_factor=0.0001285,shift_factor=0.8734)
            np.savetxt(depth_txt_path.replace('.txt','_new.txt'),new_depth_arr)
    '''
    
    ## rm the previous depth files
    depth_txt_folder_dir = '/home/gp3/Desktop/wild_gan/LapDepth-release/out_img_align_celeba_test'
    depth_txt_list = sorted(glob.glob(depth_txt_folder_dir + '/*.txt'))
    done_depth_txt_list=glob.glob(depth_txt_folder_dir + '/*new.txt')
    no_new_depth_txt_list=list(set(depth_txt_list)-set(done_depth_txt_list))
    
    for i in range(len(no_new_depth_txt_list)):
        os.system(f'rm {no_new_depth_txt_list[i]}')
    