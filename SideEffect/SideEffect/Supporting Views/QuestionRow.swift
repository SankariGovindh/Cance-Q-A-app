//
//  QuestionRow.swift
//  SideEffect
//
//  Created by Kevin Tran on 10/23/19.
//  Copyright © 2019 Kevin Tran. All rights reserved.
//

import SwiftUI

struct QuestionRow: View {
    var question: String
    var comment: [String]
    @State var newComment: String = ""
    @Environment(\.presentationMode) var presentation

    var body: some View {
        VStack(alignment: .leading) {
            Text(question)
                .bold()
                .padding()
            Divider()
            ForEach(comment, id: \.self) {
                Text("\($0)")
            }
            .padding()
            
            VStack {
                TextField("Type your comment", text: $newComment)
                .padding()
                Button(action: {
                    self.presentation.wrappedValue.dismiss()
                }) {
                    Text("Submit")
                }
            }
        }
    }
}


struct QuestionRow_Previews: PreviewProvider {
    static var previews: some View {
         Group {
            
            QuestionRow(question: NetworkManager().threadData[1].question_title, comment: NetworkManager().threadData[1].comments_text)
               }
               .previewLayout(.fixed(width: 300, height: 100))
    }
}
