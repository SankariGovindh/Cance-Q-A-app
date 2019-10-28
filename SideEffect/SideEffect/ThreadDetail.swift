//
//  ThreadDetail.swift
//  SideEffect
//
//  Created by Kevin Tran on 10/23/19.
//  Copyright © 2019 Kevin Tran. All rights reserved.
//

import SwiftUI

struct ThreadDetail:View {
    var thread: Thread
    var body: some View {
        NavigationView {
            QuestionRow(question: thread.question_title, comment: thread.comments_text)
        }
    }
}


struct ThreadDetail_Previews: PreviewProvider {
    static var previews: some View {
        ThreadDetail(thread: NetworkManager().threadData[0])
    }
}
