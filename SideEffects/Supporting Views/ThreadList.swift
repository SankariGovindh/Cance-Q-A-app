//
//  ThreadList.swift
//  SideEffects
//
//  Created by Kevin Tran on 10/31/19.
//  Copyright © 2019 Kevin Tran. All rights reserved.
//


import SwiftUI

struct ThreadList: View {
    @Environment(\.presentationMode) var presentation
    @State private var searchText = ""
    @State var networkManager = NetworkManager()
    var body: some View {
            VStack {
                HStack {
                    HStack {
                        Image(systemName: "magnifyingglass")
                        TextField("Type your question", text: $searchText, onEditingChanged: { isEditing in
//                            self.showCancelButton = true
                        }, onCommit: {
                            // QUERY FUNCTION HERE
                            print("onCommit")
                        }).foregroundColor(.primary)

                        Button(action: {
                            self.searchText = ""
                        }) {
                            Image(systemName: "xmark.circle.fill").opacity(searchText == "" ? 0 : 1)
                        }
                    }
                    .padding(EdgeInsets(top: 8, leading: 6, bottom: 8, trailing: 6))
                    .foregroundColor(.secondary)
                    .background(Color(.secondarySystemBackground))
                    .cornerRadius(10.0)

                }
                
                .padding(.horizontal)
                List(networkManager.threadData) { thread in
                    NavigationLink(destination: ThreadDetail(thread: thread)) {
                        ThreadRow(thread: thread)
                    }
                }
                
                .navigationBarTitle(Text("SideEffect"))
                .navigationBarBackButtonHidden(true)
                .navigationBarItems(trailing:
                    Button("Log Out") {
                        self.presentation.wrappedValue.dismiss()
                    }
                )
                
                NavigationLink(destination: NewQuestion()) {
                    Text("New Question")
                        .padding()
                        .foregroundColor(.white)
                        .background(LinearGradient(gradient: Gradient(colors: [Color.red,  Color.purple]), startPoint: .leading, endPoint: .trailing))
                        .cornerRadius(40)
                }.padding(.all, 5)
            }
        
    }
}

struct ThreadList_Previews: PreviewProvider {
    static var previews: some View {
        ThreadList()
    }
}
