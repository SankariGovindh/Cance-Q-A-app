//
//  Thread.swift
//  SideEffects
//
//  Created by Kevin Tran on 11/15/19.
//  Copyright © 2019 Kevin Tran. All rights reserved.
//

import SwiftUI

class Thread: Codable, Identifiable {
    var id: Int
    var user_id: String
    var username: String
    var question_username: String
    var question_user_id: Int
    var question_title: String
    var question_date_updated: String
    var question_source: String
    var question_content: String
    var question_is_anon: Bool
    var question_num_comments: Int
    var comment_username: [String]
    var comment_user_id: [Int]
    var comment_content: [String]
    var comment_source: [String]
    var comment_is_anon: [Bool]
    var comment_date_updated: [String]
}
