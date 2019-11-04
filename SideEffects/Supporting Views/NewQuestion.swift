//
//  NewQuestion.swift
//  SideEffects
//
//  Created by Kevin Tran on 10/31/19.
//  Copyright © 2019 Kevin Tran. All rights reserved.
//

import SwiftUI

struct NewQuestion: View {
    @EnvironmentObject var questionData: QuestionData
    @Environment(\.presentationMode) var presentation
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
                self.presentation.wrappedValue.dismiss()
            }) {
                Text("Submit")
                    .padding()
                    .foregroundColor(.white)
                    .background(LinearGradient(gradient: Gradient(colors: [Color.red,  Color.purple]), startPoint: .leading, endPoint: .trailing))
                    .cornerRadius(40)
            }
            /*
            Button("Submit") {
                //let dateFormatter = DateFormatter()
                //dateFormatter.dateFormat = "MM/dd/yy"
                //let thread = Thread(id: threadData.last!.id + 1, question: self.question, comment: [], date: dateFormatter.string(from: Date()))
                //add(thread: thread)
                self.presentation.wrappedValue.dismiss()
            }
            */
        }
    }
}

struct NewQuestion_Previews: PreviewProvider {
    static var previews: some View {
        NewQuestion()
    }
}
