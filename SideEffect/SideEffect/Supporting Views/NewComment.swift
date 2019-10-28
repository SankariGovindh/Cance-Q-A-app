//
//  NewComment.swift
//  SideEffect
//
//  Created by Kevin Tran on 10/24/19.
//  Copyright © 2019 Kevin Tran. All rights reserved.
//

import SwiftUI

struct NewComment: View {
    @Environment(\.presentationMode) var presentation
    @State var comment: String = ""

    var body: some View {
        VStack(alignment: .center, spacing: 30) {
            Divider()
            TextField("Type your comment", text: $comment)
            .multilineTextAlignment(.center)
            .frame(minWidth: 0, maxWidth: 350, minHeight: 0, maxHeight: 200)
            Divider()
            Button("Submit") {
                //add(thread: thread)
                self.presentation.wrappedValue.dismiss()
            }
        }
    }
}

struct NewComment_Previews: PreviewProvider {
    static var previews: some View {
        NewComment()
    }
}
