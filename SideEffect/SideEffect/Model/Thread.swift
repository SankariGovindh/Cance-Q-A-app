//
//  Thread.swift
//  SideEffect
//
//  Created by Kevin Tran on 10/23/19.
//  Copyright © 2019 Kevin Tran. All rights reserved.
//

import SwiftUI

struct Thread: Codable, Identifiable {
    var id: Int
    var question_title: String
    var question_user_id: Int
    var question_source: String
    var question_date_updated: String
    var num_comments: Int
    var comments_user_id: [Int]
    var comments_text: [String]
    var comments_source: [String]
    var comments_is_anon: [Int]
}
