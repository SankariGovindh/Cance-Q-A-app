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
    
    func create_keys_values() -> String {
        return "?username=" + username +
               "&password=" + password
    }
}

final class UserData: ObservableObject {
    @Published var username = ""
    @Published var password = ""
    @Published var firstname = ""
    @Published var lastname = ""
    @Published var email = ""
    var response = false

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

final class SearchData: ObservableObject {
    @Published var query = ""
    
    func create_keys_values() -> String {
        return "?query=" + query.replacingOccurrences(of: " ", with: "%20")
    }
}

final class userAuthData: ObservableObject {
    @Published var user_id = ""
    
    func create_keys_values() -> String {
        return "?user_id=" + user_id
    }
}
