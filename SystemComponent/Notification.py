#! python2.7
## -*- coding: utf-8 -*-

#===============================================================================
# @author: kun
# @date: 2012-06-27
#===============================================================================

import os,sys
current_path = os.getcwd()
parent_path = os.path.abspath(os.path.join(os.getcwd(), os.path.pardir))
if current_path not in sys.path:
    sys.path.append(current_path)
if parent_path not in sys.path:
    sys.path.append(parent_path)
    
from ViewParser.TreeType import CPoint

class Notification():
    '''
    Operate Android Notification 
    '''
    
    def __init__(self, tree_nodes_list):
        self.statusbar_top = 0
        self.statusbar_bottom = 37
        self.statusbar_left = 8
        self.statusbar_right = 471
        self.statusbar_height = 37
        self.statusbar_weight = 463
        
        self.tree_nodes_list = tree_nodes_list
        
        self.status_bar_class_name = "com.android.systemui.statusbar.ExpandedView"
        
        self.carrierlabel_class_name = "com.android.systemui.statusbar.CarrierLabel"
        
        self.ongoing_text = "Ongoing"
        self.ongoing_class_name = "android.widget.TextView"
        self.ongoing_id = "id/ongoingTitle"
        
        self.notifications_text = "Notifications"
        self.notifications_class_name = "android.widget.TextView"
        self.notifications_id = "id/latestTitle" 
        
        self.clear_text = "Clear"
        self.clear_button_id = "id/clear_all_button"
        
        self.item_class_name = 'com.android.systemui.statusbar.LatestItemView'
        self.item_id = "id/content"
        
    
    def getRealLocation(self, location):        
        real_location = CPoint()
        real_location.x = location.x
        real_location.y = location.y + self.statusbar_height
        
        return real_location
    
    def getCarrierInfo(self):
        for node in self.tree_nodes_list:
            if self.carrierlabel_class_name == node.mClassName:
                return node.mText
        return None 
    
    # mText : Clear
    # mId : id/clear_all_button
    def getClearButtonLocation(self):
        for node in self.tree_nodes_list:
            if (self.clear_text == node.mText) and (self.clear_button_id == node.mId):
                return self.getRealLocation(node.mLocation)
        return None
    
    def getOngoingViewNodes(self):
        view_nodes_list = []
        start_flag = False
        for node in self.tree_nodes_list:
            if (self.ongoing_class_name == node.mClassName) and (self.ongoing_id == node.mId) and (self.ongoing_text == node.mText):
                start_flag = True
                
            if (self.item_class_name == node.mClassName) and (self.item_id == node.mId) and start_flag:
                view_nodes_list.append(node)
                
            
            if (self.notifications_class_name == node.mClassName) and (self.notifications_id == node.mId) and (self.notifications_text == node.mText):
                break
        
        return view_nodes_list
    
    def getNotificationViewNodes(self):
        view_nodes_list = []
        start_flag = False
        for node in self.tree_nodes_list:
            if (self.notifications_class_name == node.mClassName) and (self.notifications_id == node.mId) and (self.notifications_text == node.mText):
                start_flag = True
                
            if (self.item_class_name == node.mClassName) and (self.item_id == node.mId) and start_flag:
                view_nodes_list.append(node)
                
        return view_nodes_list
    
    
    def getTextList(self, node):
        text_list = []
        if None==node.mChildNodes or 0==len(node.mChildNodes):
            return text_list
        
        all_child_nodes_list = []
        all_child_nodes_list.append(node)
        while 0!=len(all_child_nodes_list):
            temp_node = all_child_nodes_list.pop()
            
            if "android.widget.TextView" == temp_node.mClassName:                
                text_list.append(temp_node.mText)
                
            if (None!=temp_node.mChildNodes) and (0!=len(temp_node.mChildNodes)):
                all_child_nodes_list += temp_node.mChildNodes
                
        return text_list
                            
                
    
    
    