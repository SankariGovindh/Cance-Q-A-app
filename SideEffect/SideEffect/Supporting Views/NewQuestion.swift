//
//  NewQuestion.swift
//  SideEffect
//
//  Created by Kevin Tran on 10/23/19.
//  Copyright © 2019 Kevin Tran. All rights reserved.
//

import SwiftUI

struct NewQuestion: View {
    @Environment(\.presentationMode) var presentation
    @State var question: String = ""
    var body: some View {
        VStack(alignment: .center, spacing: 30) {
            Divider()
            TextField("Type your question", text: $question)
            .multilineTextAlignment(.center)
            .frame(minWidth: 0, maxWidth: 350, minHeight: 0, maxHeight: 200)
            Divider()
            Button("Submit") {
                //let dateFormatter = DateFormatter()
                //dateFormatter.dateFormat = "MM/dd/yy"
                //let thread = Thread(id: threadData.last!.id + 1, question: self.question, comment: [], date: dateFormatter.string(from: Date()))
                //add(thread: thread)
                self.presentation.wrappedValue.dismiss()
            }
        }
    }
}

struct NewQuestion_Previews: PreviewProvider {
    static var previews: some View {
        NewQuestion()
    }
}
