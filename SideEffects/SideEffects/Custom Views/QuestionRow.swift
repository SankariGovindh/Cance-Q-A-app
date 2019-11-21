//
//  QuestionRow.swift
//  SideEffects
//
//  Created by Kevin Tran on 11/15/19.
//  Copyright © 2019 Kevin Tran. All rights reserved.
//

import SwiftUI

struct QuestionRow: View {
    var question_id: Int
    var user_id: String
    var question_content: String
    var comment_content: [String]
    var comment_username: [String]
    var question_username: String
    
    @Environment(\.presentationMode) var presentation
    @State private var networkManager = NetworkManager()
    @EnvironmentObject var commentData: CommentData

    var body: some View {
        ScrollView {
            VStack(alignment: .leading) {
                Text(question_username)
                    .bold()
                    .padding()
                
                Text(question_content)
                    .bold()
                    .padding()
                
                Divider()
                
                ForEach(comment_content, id: \.self) {
                    Text("\($0)")
                    .padding()
                }
                .padding()
                
                VStack {
                    TextField("Type your comment", text: $commentData.comment_content)
                        .padding().textFieldStyle(RoundedBorderTextFieldStyle())
                    
                    Toggle(isOn: $commentData.comment_is_anon) {
                        Text("Post Anonymously")
                    }.padding()
                    
                    Button(action: {
                        self.commentData.question_id = String(self.question_id)
                        self.commentData.user_id = self.user_id
                        print(self.commentData)
                        self.networkManager.post(code: 4, uploadData: self.commentData.create_keys_values(), completionHandler: { flag, _  in
                            if flag == true {
                                self.presentation.wrappedValue.dismiss()
                            }
                        })
                        
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
}


struct QuestionRow_Previews: PreviewProvider {
    static var previews: some View {
        Text("Hello World")
        //QuestionRow()
    }
}
