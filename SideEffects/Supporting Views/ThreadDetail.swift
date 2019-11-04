//
//  ThreadDetail.swift
//  SideEffects
//
//  Created by Kevin Tran on 10/31/19.
//  Copyright © 2019 Kevin Tran. All rights reserved.
//

import SwiftUI

struct ThreadDetail:View {
    var thread: Thread
    var body: some View {
        QuestionRow(question_content: thread.question_content, comment_content: thread.comment_content)
    }
}


struct ThreadDetail_Previews: PreviewProvider {
    static var previews: some View {
        Text("Hello World")
        //ThreadDetail(thread: NetworkManager().threadData[0])
    }
}
