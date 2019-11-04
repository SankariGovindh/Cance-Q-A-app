//
//  QuestionRow.swift
//  SideEffects
//
//  Created by Kevin Tran on 10/31/19.
//  Copyright © 2019 Kevin Tran. All rights reserved.
//


import SwiftUI

struct QuestionRow: View {
    @EnvironmentObject var commentData: CommentData
    var question_content: String
    var comment_content: [String]
    @Environment(\.presentationMode) var presentation

    var body: some View {
        VStack {
            Text(question_content)
                .bold()
                .padding()
            Divider()
            
            ForEach(comment_content, id: \.self) {
                Text("\($0)")
            }
            .padding()
                       
            VStack {
                TextField("Type your comment", text: $commentData.comment_content)
                    .padding().textFieldStyle(RoundedBorderTextFieldStyle())
                
                Toggle(isOn: $commentData.comment_is_anon) {
                    Text("Post Anonymously")
                }.padding()
                
                Button(action: {
                    self.presentation.wrappedValue.dismiss()
                }) {
                    Text("Submit")
                        .padding()
                        .foregroundColor(.white)
                        .background(LinearGradient(gradient: Gradient(colors: [Color.red,  Color.purple]), startPoint: .leading, endPoint: .trailing))
                        .cornerRadius(40)
                }
            }
        }
    }
}


struct QuestionRow_Previews: PreviewProvider {
    static var previews: some View {
        Text("Hello World")
        /*
         Group {
            
            QuestionRow(question: NetworkManager().threadData[1].question_title, comment: NetworkManager().threadData[1].comments_text)
               }
               .previewLayout(.fixed(width: 300, height: 100))
        */
    }
}
