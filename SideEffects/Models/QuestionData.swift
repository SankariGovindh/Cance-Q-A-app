//
//  QuestionData.swift
//  SideEffects
//
//  Created by Kevin Tran on 11/1/19.
//  Copyright © 2019 Kevin Tran. All rights reserved.
//

import Combine
import SwiftUI

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
               "&question_title=" + question_title +
               "&question_content=" + question_content +
               "&question_is_anon=" + String(question_is_anon)
    }
}
