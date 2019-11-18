//
//  MainView.swift
//  SideEffects
//
//  Created by Kevin Tran on 11/15/19.
//  Copyright © 2019 Kevin Tran. All rights reserved.
//

import SwiftUI

struct MainView: View {
    @State var isAddPresented = false
    @Environment(\.presentationMode) var presentation
    
    @EnvironmentObject var searchData: SearchData
    @EnvironmentObject var userAuthData: userAuthData
    @Binding var networkManager: NetworkManager
    
    var body: some View {
        VStack {
            HStack {
                HStack {
                    Image(systemName: "magnifyingglass")
                    TextField("Type your question", text: $searchData.query, onEditingChanged: { isEditing in
                        }, onCommit: {
                            print(self.searchData.query)
                            self.networkManager.post(code: 13, uploadData: self.searchData.create_keys_values()) { (flag, data) in
                                if flag == true {
                                    self.networkManager.decodeThread(data: data!)
                                }
                            }
                    }).foregroundColor(.primary)

                    Button(action: {
                        self.searchData.query = ""
                    }) {
                        Image(systemName: "xmark.circle.fill").opacity(self.searchData.query == "" ? 0 : 1)
                    }
                }
                .padding(EdgeInsets(top: 8, leading: 6, bottom: 8, trailing: 6))
                .foregroundColor(.secondary)
                .background(Color(.secondarySystemBackground))
                .cornerRadius(10.0)

            }
            .padding(.horizontal)
            
            List(networkManager.threadData) { thread in
                NavigationLink(destination: ThreadDetailRow(thread: thread)) {
                    ThreadRow(thread: thread)
                }
            }
            
            .navigationBarTitle(Text("SideEffect"))
            .navigationBarBackButtonHidden(true)
            .navigationBarItems(trailing:
                
                Button("Log Out") {
                    self.networkManager.post(code: 12, uploadData: "", completionHandler: { flag, _  in
                        if flag == true {
                            self.presentation.wrappedValue.dismiss()
                        }
                    })
                    self.presentation.wrappedValue.dismiss()
                }
            )
            HStack {
                NavigationLink(destination: NewQuestionRow(networkManager: self.networkManager)) {
                    Image(systemName: "plus.bubble.fill")
                        .padding()
                        .foregroundColor(.white)
                        .background(LinearGradient(gradient: Gradient(colors: [Color.red, Color.purple]), startPoint: .leading, endPoint: .trailing))
                        .cornerRadius(40)
                }.padding(.all, 5)
                
                Spacer().frame(width: 50)
                
                
                Button(action: {
                    self.userAuthData.user_id = self.networkManager.threadData[0].user_id
                    
                    self.networkManager.post(code: 11, uploadData: self.userAuthData.create_keys_values()) { (flag, data) in
                        if flag == true {
                            self.networkManager.decodeUserThread(data: data!)
                        }
                    }
                }) {
                    NavigationLink(destination: ProfileView(networkManager: self.networkManager)) {
                        Image(systemName: "person.fill")
                            .padding()
                            .foregroundColor(.white)
                            .background(LinearGradient(gradient: Gradient(colors: [Color.red, Color.purple]), startPoint: .leading, endPoint: .trailing))
                            .cornerRadius(40)
                    }.padding(.all, 5)
                }
            }
        }
    }
}

struct MainView_Previews: PreviewProvider {
    static var previews: some View {
        Text("Hello World")
        //MainView()
    }
}
