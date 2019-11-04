//
//  CommentData.swift
//  SideEffects
//
//  Created by Kevin Tran on 11/1/19.
//  Copyright © 2019 Kevin Tran. All rights reserved.
//

import Combine
import SwiftUI

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
               "&comment_content=" + comment_content +
               "&comment_is_anon=" + String(comment_is_anon)
    }
}
