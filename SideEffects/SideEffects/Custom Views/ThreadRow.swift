//
//  ThreadRow.swift
//  SideEffects
//
//  Created by Kevin Tran on 11/15/19.
//  Copyright © 2019 Kevin Tran. All rights reserved.
//

import SwiftUI

struct ThreadRow: View {
    var thread: Thread
    var body: some View {
        VStack(alignment: .leading) {
            Text(verbatim: thread.question_username)
                .bold()
            Text(verbatim: thread.question_content)
        }
        .frame(height: 100)
    }
}

struct ThreadRow_Previews: PreviewProvider {
    static var previews: some View {
        Text("Hello World")
    }
}
