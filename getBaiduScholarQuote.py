# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 08:18:13 2020

@author: CJH
"""
import os
import tkinter
from tkinter import filedialog
from selenium import webdriver
from time import sleep

'''
判断元素是否存在
'''
def isElementExist(driver, element):
    flag = True
    try:
        driver.find_element_by_xpath(element)
        return flag
 
    except:
        flag = False
        return flag
    
'''
select file by the UI
'''
root = tkinter.Tk()
root.withdraw()

default_dir = os.path.expanduser('~')
filePath = filedialog.askopenfilenames(title='selectFile',initialdir=default_dir)
filePath = list(filePath)

if len(filePath):

    Listfilename=[]
    for fliePathIndex in filePath:
        (tempfilePath, tempfilename) = os.path.split(fliePathIndex)
        (tempfilename, tempextension) = os.path.splitext(tempfilename)
        Listfilename.append(tempfilename)
    
    '''
    open the browser
    '''
    base_url = "https://xueshu.baidu.com/"
    driver_url = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedgedriver.exe"
    result = []
    
    dri = webdriver.Edge(executable_path=driver_url)
    dri.get(base_url)
    sleep(2)
    
    '''
    get the  quote 
    '''
    for tempListfilename in Listfilename:
        dri.find_element_by_xpath('//*[@id="kw"]').send_keys(tempListfilename)
        sleep(2)
        dri.find_element_by_xpath('//*[@id="su"]').click()
        sleep(2)
        
        if isElementExist(dri,'//*[@id="toolbar"]/span'):
            dri.find_element_by_xpath('//*[@id="1"]/div[2]/div/a[2]').click()
            sleep(2)
        else:
            dri.find_element_by_xpath('//*[@id="dtl_l"]/div[1]/div[3]/div/a[2]').click()
            sleep(2)
        try:
            tempresult = dri.find_element_by_xpath('//*[@data-type="GB/T"]/p').text
        except:
            tempresult = '引用出错'
    
        result.append(tempresult)
    
        dri.back()
        sleep(2)
    
    '''
    close the browser     
    '''
    dri.close()
    '''
    input file name
    '''
    txtName = input('input txt file name：')
    txtName = txtName+'.txt'
    
    '''
    write 
    '''
    with open(txtName,'w+') as writeFile:
        for index,quote in enumerate(result):
            writeFile.write('[{0}]{1}\n'.format(index+1,quote))
else:
    print('取消操作')        

