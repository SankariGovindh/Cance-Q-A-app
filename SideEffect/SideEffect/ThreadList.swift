//
//  ContentView.swift
//  SideEffect
//
//  Created by Kevin Tran on 10/23/19.
//  Copyright © 2019 Kevin Tran. All rights reserved.
//

import SwiftUI
import SwiftUI

struct ThreadList: View {
    @State private var searchText = ""
    @State var networkManager = NetworkManager()
    var body: some View {
        NavigationView {
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
                NavigationLink(destination: NewQuestion()) {
                    Text("New Question")
                    .padding(.all)
                }.padding(.all, 5)
            }
        }
    }
}

struct ThreadList_Previews: PreviewProvider {
    static var previews: some View {
        ThreadList()
    }
}
