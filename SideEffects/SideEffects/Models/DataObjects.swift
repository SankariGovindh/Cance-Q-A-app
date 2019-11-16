//
//  DataObjects.swift
//  SideEffects
//
//  Created by Kevin Tran on 11/15/19.
//  Copyright © 2019 Kevin Tran. All rights reserved.
//

import Combine
import SwiftUI

final class LoginData: ObservableObject  {
    @Published var username = ""
    @Published var password = ""
    
    func validate() -> Bool {
        if username == "" || password == "" { return false }
        return true
    }
    
    func create_keys_values() -> String {
        return "?username=" + username +
               "&password=" + password
    }
    
    func post(networkManager: NetworkManager) -> Bool {
        if validate() {
            if networkManager.post(code: 1, uploadData: create_keys_values()) {
                username = ""
                password = ""
            }
            
            return true
        }
        
        return false
    }
}

final class UserData: ObservableObject {
    @Published var username = ""
    @Published var password = ""
    @Published var firstname = ""
    @Published var lastname = ""
    @Published var email = ""
    
    func validate() -> Bool {
        if username == "" || password == "" ||
           firstname == "" || lastname == "" ||
           email == "" { return false }
        return true
    }

    func create_keys_values() -> String {
        return "?username=" + username +
               "&password=" + password +
               "&first_name=" + firstname +
               "&last_name=" + lastname +
               "&email=" + email
    }
    
    func post(networkManager: NetworkManager) -> Bool {
        if validate() {
            if networkManager.post(code: 2, uploadData: create_keys_values()) {
                firstname = ""
                lastname = ""
                username = ""
                password = ""
                email = ""
            }
            
            return true
        }
        
        return false
    }
}

final class QuestionData: ObservableObject  {
    @Published var user_id = ""
    @Published var question_title = ""
    @Published var question_content = ""
    @Published var question_is_anon = true
    
    func validate() -> Bool {
        if question_title == "" || question_content == "" { return false }
        return true
    }
    
    func create_keys_values() -> String {
        return "?user_id=" + user_id +
               "&title=" + question_title +
               "&content=" + question_content +
               "&is_anonymous=" + String(question_is_anon == true ? 1 : 0) +
               "&source=" + "SideEffects"
    }
}

final class CommentData: ObservableObject  {
    @Published var user_id = ""
    @Published var question_id = ""
    @Published var comment_content = ""
    @Published var comment_is_anon = true
    
    func validate() -> Bool {
        if comment_content == "" { return false }
        return true
    }
    
    func create_keys_values() -> String {
        return "?user_id=" + user_id +
               "&question_id=" + question_id +
               "&content=" + comment_content +
               "&is_anonymous=" + String(comment_is_anon == true ? 1 : 0) +
               "&source=" + "SideEffects"
    }
}
