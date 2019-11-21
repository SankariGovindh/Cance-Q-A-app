//
//  NewQuestionRow.swift
//  SideEffects
//
//  Created by Kevin Tran on 11/16/19.
//  Copyright © 2019 Kevin Tran. All rights reserved.
//

import SwiftUI


import SwiftUI

struct NewQuestionRow: View {
    @EnvironmentObject var questionData: QuestionData
    @Environment(\.presentationMode) var presentation
    @State var networkManager: NetworkManager
    
    var body: some View {
        VStack(alignment: .center, spacing: 30) {
            HStack {
                Text("Header")
                TextField("Question Title", text: $questionData.question_title)
                    .multilineTextAlignment(.center)
                    .textFieldStyle(RoundedBorderTextFieldStyle())
            }.padding()
            
            Divider()
            
            TextField("Type your question", text: $questionData.question_content)
                .multilineTextAlignment(.center)
                .frame(minWidth: 0, maxWidth: 350, minHeight: 0, maxHeight: 200)
                .textFieldStyle(RoundedBorderTextFieldStyle())
            
            Divider()
            
            Toggle(isOn: $questionData.question_is_anon) {
                Text("Post Anonymously")
            }.padding()
            
            Button(action: {
                self.questionData.user_id = self.networkManager.threadData[0].user_id
                self.networkManager.post(code: 3, uploadData: self.questionData.create_keys_values(), completionHandler: { flag, data  in
                    if flag == true {
                        self.networkManager.decodeThread(data: data!)
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

struct NewQuestionRow_Previews: PreviewProvider {
    static var previews: some View {
        Text("Hello World")
       // NewQuestionRow()
    }
}
