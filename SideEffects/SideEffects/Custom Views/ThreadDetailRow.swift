//
//  ThreadDetailRow.swift
//  SideEffects
//
//  Created by Kevin Tran on 11/16/19.
//  Copyright © 2019 Kevin Tran. All rights reserved.
//

import SwiftUI

struct ThreadDetailRow: View {
    var thread: Thread
    var body: some View {
        QuestionRow(question_id: thread.id, user_id: thread.user_id, question_content: thread.question_content, comment_content: thread.comment_content, comment_username: thread.comment_username, question_username: thread.question_username)
    }
}

struct ThreadDetailRow_Previews: PreviewProvider {
    static var previews: some View {
        Text("Hello")
    }
}
